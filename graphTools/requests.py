request_by_title = """
    PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>
    PREFIX ecrm:  <http://erlangen-crm.org/current/> 

    SELECT Distinct ?p ?P102_has_title
    WHERE{
        ?p a efrbroo:F22_Self-Contained_Expression;
         ecrm:P102_has_title ?P102_has_title.
}
"""

request_by_catalogue = """
      PREFIX mus: <http://data.doremus.org/ontology#> 
       PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>

    SELECT  Distinct ?p ?U16_has_catalogue_statement 
    WHERE {
         ?p a efrbroo:F22_Self-Contained_Expression;
         mus:U16_has_catalogue_statement ?U16_has_catalogue_statement.

    }
"""

request_by_note = """
    PREFIX ecrm:  <http://erlangen-crm.org/current/> 
    PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>
    SELECT DISTINCT ?p ?P3_has_note 
    WHERE {
         ?p a efrbroo:F22_Self-Contained_Expression;
         ecrm:P3_has_note ?P3_has_note .
    }
"""

request_by_genre = """
    PREFIX mus: <http://data.doremus.org/ontology#> 
    PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>

    SELECT  Distinct ?p ?U12_has_genre 
    WHERE {
         ?p a efrbroo:F22_Self-Contained_Expression;
         mus:U12_has_genre ?U12_has_genre .

    }
"""
request_by_key = """
    PREFIX mus: <http://data.doremus.org/ontology#> 
    PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>

    SELECT Distinct ?p ?U11_has_key 
    WHERE {
        ?p a efrbroo:F22_Self-Contained_Expression; 
        mus:U11_has_key ?U11_has_key .

    }
"""

request_by_casting = """
    PREFIX mus: <http://data.doremus.org/ontology#> 
    PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>

    SELECT Distinct ?p ?U13_has_casting 
    WHERE {
        ?p a efrbroo:F22_Self-Contained_Expression; 
        mus:U13_has_casting ?U13_has_casting.

    }
"""


