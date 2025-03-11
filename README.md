# DEZSYS_EK_WAREHOUSE_MICROSERVICE_PY

# Middleware Engineering "Microservices" - Taskdescription  

Join GIT repository:   [git@github.com:ThomasMicheler/DEZSYS_EK_WAREHOUSE_MICROSERVICE_PY.git](git@github.com:ThomasMicheler/DEZSYS_EK_WAREHOUSE_MICROSERVICE_PY.git)

## 1. Einführung

Diese Übung soll helfen die Funktionsweise und Einsatzmöglichkeiten von Microservices in dezentralen Systemen zu verstehen. Anhand eines Tutorials wird ein Microservice implementiert in verschiedenen Anwendungsbereichen implementiert werden.

## 2. Ziele

Das Ziel dieser Übung ist die Implementierung eines Microservices und die Einbindung in ein bestehendes Middleware-System.

## 3. Voraussetzungen

* Grundlagen Python
* [Grundlagen Microservices](https://www.edureka.co/blog/what-is-microservices/)

## 4. Aufgabenstellung

Führen Sie die einzelnen Schritte des Tutorials ["Building a Simple Microservices Architecture with Python: A Step-by-Step Guide"](https://medium.com/@bittusinghtech/building-a-simple-microservices-architecture-with-python-a-step-by-step-guide-c41da2cd4631) durch und implementieren Sie folgende Erweiterungen:

## 5. Demo Applikation

* Erstellen der Applikation, wie im Tutorial beschrieben und starten der Microservices als Webapplikation.  

* Starten der Microservice User:
  `uvicorn main:app --reload --port 8001`  

* Starten der Microservice Productr:
  `uvicorn main:app --reload --port 8002`  

* Starten der Microservice Order:
  `uvicorn main:app --reload --port 8003`  

## 6. Bewertung
Gruppengrösse: 1 Person  

### 6.1 Erweiterte Anforderungen **überwiegend erfüllt**
- Durchlesen des Tutorials " ["Building a Simple Microservices Architecture with Python: A Step-by-Step Guide"](https://medium.com/@bittusinghtech/building-a-simple-microservices-architecture-with-python-a-step-by-step-guide-c41da2cd4631) "
- Implementieren die neuen Funktionen, wie unter Punkt 4 beschrieben
- **Einzelne Schritte und Komponenten des Beispiels verstehen und im Protokoll dokumentieren**
- Beantwortung der Fragestellungen  

### 6.2 Erweiterte Anforderungen **zur Gänze erfüllt**
- Entwickeln Sie ein weiteres Microservice (Teil 2) zu dem Data Warehouse Beispiel (Port 4441)
- Dieses Microservice ist fuer die Speicherung der Data Warehouse Daten verantwortlich. Mit diesem Microservice wird ein NoSQL-Repository (MongoDB) und ein Service zum Empfangen und Speicher der Daten zur Verfuegung gestellt.
- **Alle Erweiterungen im Protokoll erklaeren und dokumentieren**

## 7. Fragestellung für Protokoll

+ Was versteht man unter Microservices?
+ Stellen Sie anhand eines Beispiels den Einsatz von Microservices dar.
+ Wie kann man Spring Cloud nutzen und welche Tools werden dabei unterstützt?
+ Beschreiben Sie das Spring Cloud Netflix Projekt. Aus welchen Bestandteilen setzt sich dieses Projekt zusammen?
+ Wofür werden die Annotations @EnableEurekaServer und @EnableDiscoveryClient verwendet?
+ Wie werden in dem Account Service die Properties gesetzt und welche Parameter werden hier verwendet?
+ Wie funktioniert das Logging bei diesem Beispiel? Ist es möglich das Logging zu erhöhen bzw. komplett abzudrehen?
  Wenn ja, wie?
+ Definition des Begriffs "**Service Mesh**"
+ Was sind die **Funktionalitaeten** eines "Service Mesh"?
+ Recherchieren nach **2 bekannten Herstellern** eines "Service Mesh" und beschreiben kurz deren Funktionsumfang
+ **Stellen Sie die 2 Produkte gegenueber und vergleichen Sie diese**

## 8. Links und Dokumente
* [Microservices with Spring](https://spring.io/blog/2015/07/14/microservices-with-spring)
* [Microservices with Spring Boot](https://medium.com/omarelgabrys-blog/microservices-with-spring-boot-intro-to-microservices-part-1-c0d24cd422c3)
* [Eureka – Microservice-Registry mit Spring Cloud](https://www.heise.de/developer/artikel/Eureka-Microservice-Registry-mit-Spring-Cloud-2848238.html?seite=all)
* [Spring Boot Tutorial: In 10 Schritten zur Microservices-Architektur](https://jaxenter.de/spring-boot-tutorial-microservices-cloud-foundry-kubernetes-58695)
* [Introducing Spring Cloud](https://spring.io/blog/2014/06/03/introducing-spring-cloud)
