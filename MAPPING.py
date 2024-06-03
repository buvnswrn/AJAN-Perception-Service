PEOPLE_COUNT = """
@prefix ex: <http://example.org/> .
@prefix schema: <http://schema.org/> .
@prefix rml: <http://semweb.mmlab.be/ns/rml#> .
@prefix rr: <http://www.w3.org/ns/r2rml#> .
@prefix ql: <http://semweb.mmlab.be/ns/ql#> .
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:Street
    rr:subjectMap [
        rr:template "http://example.org/street" ;
        rr:class ex:Street ;
    ] ;
    rr:predicateObjectMap [
        rr:predicate schema:description ;
        rr:objectMap [
        rml:reference "description" ;
        ] ;
    ] ;
    rr:predicateObjectMap [
        rr:predicate schema:location ;
        rr:objectMap [
        rml:reference "location" ;
        ] ;
    ] ;
    rr:predicateObjectMap [
        rr:predicate schema:people ;
        rr:objectMap [
        rml:reference "people" ;
        ] ;
    ];
    rr:predicateObjectMap [
       rr:predicate schema:count ;
         rr:objectMap [
            rml:reference "count" ;
            ] ;
    ] .
"""

SIGNAL_ON_OFF = """
@prefix ex: <http://example.org/> .
@prefix schema: <http://schema.org/> .
@prefix rml: <http://semweb.mmlab.be/ns/rml#> .
@prefix rr: <http://www.w3.org/ns/r2rml#> .
@prefix ql: <http://semweb.mmlab.be/ns/ql#> .
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:Signal
    rr:subjectMap [
        rr:template "http://example.org/signal" ;
        rr:class ex:Signal ;
    ] ;
    rr:predicateObjectMap [
        rr:predicate schema:description ;
        rr:objectMap [
        rml:reference "description" ;
        ] ;
    ] ;
    rr:predicateObjectMap [
        rr:predicate schema:color ;
        rr:objectMap [
        rml:reference "color" ;
        ] ;
    ] .
"""