from rdflib import Graph

from graphTools.Similarity import *
from graphTools.requests import *


class Graphtools(object):
    def __init__(self, source, target, output):
        self.g2 = None
        self.g1 = None
        self.urlSource = source
        self.urlTarget = target
        self.fichier = open(output, "w")

    def setup(self):
        self.g1 = Graph()
        self.g2 = Graph()
        self.g1.parse(self.urlSource, format='ttl')
        self.g2.parse(self.urlTarget, format='ttl')

    def function_comp_title(self, similarity_method, threshold, progressbar):
        source = self.g1.query(request_by_title)
        target = self.g2.query(request_by_title)
        counter = 0
        total = len(source)
        line_seen = set()
        for s in source:
            counter += 1
            progressbar.setValue((counter * 100) / total)
            for t in target:
                score = round(calculate_avg_similarity(similarity_method, str(s["P102_has_title"]),
                                                       str(t["P102_has_title"])), 2)
                if score <= threshold:
                    line = "<" + str(s["p"]) + ">  <http://www.w3.org/2002/07/owl#sameAs>  <" + str(
                        t["p"]) + "> .\n"
                    if line not in line_seen:  # not a duplicate
                        line_seen.add(line)
                        self.fichier.write(line)
        self.fichier.close()

    def request_by_catalogue(self, similarity_method, threshold, progressbar):
        source = self.g1.query(request_by_catalogue)
        target = self.g2.query(request_by_catalogue)
        counter = 0
        total = len(source)
        line_seen = set()
        for s in source:
            counter += 1
            progressbar.setValue((counter * 100) / total)
            for t in target:
                score = calculate_avg_similarity(similarity_method, str(s["U16_has_catalogue_statement"]),
                                                 str(t["U16_has_catalogue_statement"]))
                if score <= threshold:
                    line = "<" + str(s["p"]) + "> <http://www.w3.org/2002/07/owl#sameAs> <" + str(
                        t["p"]) + ">.\n"
                    if line not in line_seen:  # not a duplicate
                        line_seen.add(line)
                        self.fichier.write(line)
        self.fichier.close()

    def function_comp_note(self, similarity_method, threshold, progressbar):
        source = self.g1.query(request_by_note)
        target = self.g2.query(request_by_note)
        counter = 0
        line_seen = set()
        total = len(source)
        for s in source:
            counter += 1
            progressbar.setValue((counter * 100) / total)
            for t in target:
                score = calculate_avg_similarity(similarity_method, str(s["P3_has_note"]),
                                                 str(t["P3_has_note"]))
                if score <= threshold:
                    line = "<" + str(s["p"]) + "> <http://www.w3.org/2002/07/owl#sameAs> <" + str(
                        t["p"]) + ">.\n"
                    if line not in line_seen:  # not a duplicate
                        line_seen.add(line)
                        self.fichier.write(line)
        self.fichier.close()

    def function_comp_genre(self, similarity_method, threshold, progressbar):
        source = self.g1.query(request_by_genre)
        target = self.g2.query(request_by_genre)
        counter = 0
        line_seen = set()
        total = len(source)
        for s in source:
            counter += 1
            progressbar.setValue((counter * 100) / total)
            for t in target:
                score = round(calculate_avg_similarity(similarity_method, str(s["U12_has_genre"]),
                                                       str(t["U12_has_genre"])), 2)
                if score <= threshold:
                    line = "<" + str(s["p"]) + "> <http://www.w3.org/2002/07/owl#sameAs> <" + str(
                        t["p"]) + ">.\n"
                    if line not in line_seen:  # not a duplicate
                        line_seen.add(line)
                        self.fichier.write(line)

        self.fichier.close()

    def function_comp_key(self, similarity_method, threshold, progressbar):
        source = self.g1.query(request_by_key)
        target = self.g2.query(request_by_key)
        counter = 0
        line_seen = set()
        total = len(source)
        for s in source:
            counter += 1
            progressbar.setValue((counter * 100) / total)
            for t in target:
                score = calculate_avg_similarity(similarity_method, str(s["U11_has_key"]),
                                                 str(t["U11_has_key"]))
                if score <= threshold:
                    line = "<" + str(s["p"]) + ">  <http://www.w3.org/2002/07/owl#sameAs>  <" + str(
                        t["p"]) + "> .\n"
                    if line not in line_seen:  # not a duplicate
                        line_seen.add(line)
                        self.fichier.write(line)
        self.fichier.close()

    def function_comp_casting(self, similarity_method, threshold, progressbar):
        source = self.g1.query(request_by_casting)
        target = self.g2.query(request_by_casting)
        counter = 0
        line_seen = set()
        total = len(source)
        for s in source:
            counter += 1
            progressbar.setValue((counter * 100) / total)
            for t in target:
                score = calculate_avg_similarity(similarity_method, str(s["U13_has_casting"]),
                                                 str(t["U13_has_casting"]))
                if score <= threshold:
                    line = "<" + str(s["p"]) + "> <http://www.w3.org/2002/07/owl#sameAs> <" + str(
                        t["p"]) + ">.\n"
                    if line not in line_seen:  # not a duplicate
                        line_seen.add(line)
                        self.fichier.write(line)
        self.fichier.close()




