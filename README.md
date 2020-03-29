# Knowledge Graph To The Rescue Covid-19
This Repository will be used to maintain/ aware people about KG for Covid-19
### Currently, I'm working with team where we have multiple projects. My target is to make a Semantic Query Engine backed with Knowledge Graph.
### Step 1:
<ul><li> Grab and integrate data sources and enrich Knowledge in Graph</li></ul>

### Step 2:
<ul><li> Devise Semantic Queries</li></ul>

### Step 3:
<ul><li> Integrate Semantic Queries with KG </li></ul>

# Tools:
#### Neo4j (My First Graph Database Love!)
#### Python (Flask)

# Graph Model

<img src= "https://github.com/Siraj1munir/KG_to_the_rescue_covid-19/blob/master/Graph_model_for_KG_NEO4j_Update.jpg">

# Project Introduction
[KG To The Rescue Video Introduction!](https://github.com/Siraj1munir/KG_to_the_rescue_covid-19/blob/master/Intro_to_project.mp4 "KG To The Rescue")
# First Sprint of KG
So till now what you can do with my KG

### Here are some queries that you can do with this version of Knowledge Graph
#### Note: Username: neo4j and Password: 123
~~~ Find Region Specific Knowlege:
MATCH (n:Location) WHERE n.Region= "China" RETURN n 
~~~
~~~
Find Region and Time driven Knowledge:
MATCH (n:Location) WHERE n.Region= "China" AND n.Last_Update= "2020-03-11T10:53:02" RETURN n
~~~
~~~ 

Find Region and Province Based Knowledge
MATCH (n:Location) WHERE n.Region= "China" AND n.Province= "Hubei" AND n.Last_Update= "2020-03-11T10:53:02"  RETURN n
~~~
~~~ 
Region with Recovered Cases:
MATCH (n:Location) WHERE n.Region= "Pakistan" AND n.Recovered= "13" RETURN n
Similarly can find Deaths/fitalities 
~~~
~~~ 
Trackdown Location status in Date wise manner:
MATCH (n:Location) WHERE n.Location_Name= "Pakistan" AND n.date= "2020-03-20" RETURN n 
~~~
