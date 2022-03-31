from math import floor

from strsimpy.jaro_winkler import JaroWinkler
from strsimpy.levenshtein import Levenshtein

levenshtein = Levenshtein()
jarowinkler = JaroWinkler()


def jaccard(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return 1 - float(intersection) / union


def jaro_distance(s1, s2):
    # If the s are equal
    if s1 == s2:
        return 0.0

    len1 = len(s1)
    len2 = len(s2)
    max_dist = floor(max(len1, len2) / 2) - 1
    match = 0
    hash_s1 = [0] * len(s1)
    hash_s2 = [0] * len(s2)

    for i in range(len1):
        for j in range(max(0, i - max_dist),
                       min(len2, i + max_dist + 1)):

            if s1[i] == s2[j] and hash_s2[j] == 0:
                hash_s1[i] = 1
                hash_s2[j] = 1
                match += 1
                break

    if match == 0:
        return 1.0
    t = 0
    point = 0
    for i in range(len1):
        if hash_s1[i]:
            while hash_s2[point] == 0:
                point += 1

            if s1[i] != s2[point]:
                t += 1
            point += 1
    t = t // 2
    return 1 - ((match / len1 + match / len2 + (match - t) / match) / 3.0)


def calculate_avg_similarity(list_method, text1, text2):
    score = 0
    divided_by = 0
    for i in list_method:
        final_measure = i.split(":")
        if final_measure[0] == "Levenshtein":
           # print("LEV: ", levenshtein.distance(text1, text2) / max(len(text1), len(text2)) * float(final_measure[1]))
            #print("SCORE: ", score)
            score += levenshtein.distance(text1, text2) / max(len(text1), len(text2)) * float(final_measure[1])
            divided_by += float(final_measure[1])
        elif final_measure[0] == "Jaro":
            score += jaro_distance(text1, text2) * float(final_measure[1])
            divided_by += float(final_measure[1])
        elif final_measure[0] == "Jaro Winkler":
            score += jarowinkler.distance(text1, text2) * float(final_measure[1])
            divided_by += float(final_measure[1])
        elif final_measure[0] == "Jaccard":
            score += jaccard(text1, text2) * float(final_measure[1])
            divided_by += float(final_measure[1])
    return round(score / divided_by, 2)
