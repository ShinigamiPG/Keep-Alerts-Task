# Keep-Alerts-Task
Coding Task Description : For a practical coding task, let’s say we need more data for a training dataset. We decide to create a service based on an artificial dataset. Using the attached JSONs, design and execute the solution to generate the dataset of one thousand correlated alerts. Feel free to use third-party datasets and models.

The assignment description is intentionally vague to give you decision-making freedom, similar to what we expect in the actual work routine for this role. While designing the system, please make assumptions about missing requirements and be ready to share those assumptions explicitly.


Files Overview : 
Alert_prom.json - JSON 1
Alert_home.json - JSON 2
Data.py - Contains generated/curated data required for the task
Main.py - Code for the task
Generated Alerts.zip - A set of 1000 generated alerts (Output of the task)

Approach : 
1) In each JSON, select the tags which are potentially relevant for correlation.
2) Obtain data/lists of entries which could be suitable for these tags.
3) From the skeleton of the JSON's, generate new ones using the obtained data.

   Relevant tags for JSON1 - ['name', 'env', 'region', 'severity', 'instance',  'startsAt',   'endsAt', 'description', 'fingerprint']
   
   Relevant tags for JSON2 - ['name', 'severity', 'message']

Assumptions:
1) Alerts are monitored in a 2-hr time window from 8 to 10 am on 12/07/2024.
2) Since the model wont use tags irrelevant for correlation , the remaining tags are filled with random strings.
3) Skeleton of JSON 1 was altered to remove repeating tags.
