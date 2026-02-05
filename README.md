
#ETL  DATA PIPELINE ON GCP(GOOGLE CLOUD PLATFORM) WITH CLOUD DATA FUSION AND AIRFLOW
 
 
 TASK:
 
 Create data pipeline to extract employee data from various sources, mask the sensitive data within data and load to BigQuery.
 Create a dashboard to visualize the  the employee data securely.
 
 REQUIREMENTS:
 
 Data Extraction: Extract employee data from multiple sources such as databases, CSV files, APIs.
 
 Data Masking: Identify the sensitive data within employee data such as salary,bankdetails, personal info.
 
 Data Loading into bigquery: securly load the  extracted data into bigquery.
 
 Dashboard( visualization): design a webbased dashboard( google data studio, tabuleau,etc.,)
 
 
 CLOUD RESOUCES:
 
 Cloud storage: To store the data 
 Data Fusion: It is an no code solution to transform sensitive data into non visible data when it is in public domain.
 Bigquery: It is to load data that was transformed
 Airflow: we orchestrate this pipeline on cloud composer using airflow.
 
PROGRAMMING LANGUAGE:

python
