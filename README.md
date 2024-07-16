# Keep-Alerts-Task
# Design Task: 
time used - 20 min

**Description :** 
Alert is a free-form JSON coming from Providers. Each Provider has its own Alert structure.

For instance, the provider Prometheus may generate alerts , while a customer’s homegrown alert system may present a different structure.

Build a detailed architecture description (AI part) for an alert correlation micro-service. Its purpose is to correlate alerts to existing “Incidents” or create new Incidents. 

The service’s input:

- List (and some description) of “services” (system components),
- Information about past incidents,
- New alerts,
- Past (already correlated alerts),
- Ongoing incidents.

Service output:

- Should alerts be correlated to an existing Incident(s)?
    - If yes:
        - What’s the Incident correlate them to?
    - If not:
        - Should the new Incident be initiated? Why was it initiated? What’s this Incident about?
     
**Solution :**

I came up with this approach based on my knowledge from university courses and independent research.

RAG Approach with LLM :

1) JSON Alert as input.
2) Create a vector database of the incident and alert history and index it according to their embeddings.
3) For each incoming alert retrieve top 10 incident(s) from the DB which clear a similarity threshold. 
4) Prompt an LLM like GPT the following - "Given the following alert: {alert_json}, and these related incidents: {incidents_json}, should this alert be grouped with an existing incident or should a new incident be created?"



# Coding Task:


**Description : **For a practical coding task, let’s say we need more data for a training dataset. We decide to create a service based on an artificial dataset. Using the attached JSONs, design and execute the solution to generate the dataset of one thousand correlated alerts. Feel free to use third-party datasets and models.

The assignment description is intentionally vague to give you decision-making freedom, similar to what we expect in the actual work routine for this role. While designing the system, please make assumptions about missing requirements and be ready to share those assumptions explicitly.

**
Files Overview : **

Alert_prom.json - JSON 1

Alert_home.json - JSON 2

Data.py - Contains generated/curated data required for the task

Main.py - Code for the task

Generated Alerts.zip - A set of 1000 generated alerts (Output of the task)

**Approach : **
1) In each JSON, select the tags which are potentially relevant for correlation.
2) Obtain data/lists of entries which could be suitable for these tags.
3) From the skeleton of the JSON's, generate new ones using the obtained data.

   Relevant tags for JSON1 - ['name', 'env', 'region', 'severity', 'instance',  'startsAt',   'endsAt', 'description', 'fingerprint']
   
   Relevant tags for JSON2 - ['name', 'severity', 'message']

Assumptions:
1) Alerts are monitored in a 2-hr time window from 8 to 10 am on 12/07/2024.
2) Since the model wont use tags irrelevant for correlation , those tags are filled with random strings.
3) Skeleton of JSON 1 was altered to remove repeating tags.
