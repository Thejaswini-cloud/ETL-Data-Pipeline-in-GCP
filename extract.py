import pandas as pd
from faker import Faker
import random
from google.cloud import storage
from io import BytesIO

# Initialize Faker and seeds
fake = Faker()
Faker.seed(42)
random.seed(42)

# Generate employee data
def generate_employee(emp_id):
    return {
        "employee_id": emp_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "gender": random.choice(["Male", "Female", "Other"]),
        "date_of_birth": fake.date_of_birth(minimum_age=21, maximum_age=65),
        "ssn": fake.ssn(),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "address": fake.address().replace("\n", ", "),
        "job_title": fake.job(),
        "department": random.choice([
            "Engineering", "HR", "Finance", "Sales", "Marketing", "Operations"
        ]),
        "salary": random.randint(50000, 180000),
        "hire_date": fake.date_between(start_date="-10y", end_date="today"),
        "manager_name": fake.name()
    }

num_employees = 100
employees = [generate_employee(i + 1) for i in range(num_employees)]
df = pd.DataFrame(employees)

# Upload to GCS directly from memory
def upload_df_to_gcs(df, bucket_name, destination_blob_name):
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        # Convert DataFrame to CSV bytes
        csv_buffer = BytesIO()
        df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)  # Move to the start of the buffer

        # Upload CSV bytes
        blob.upload_from_file(csv_buffer, content_type="text/csv")
        print(f"Uploaded successfully to gs://{bucket_name}/{destination_blob_name}")
    except Exception as e:
        print("Upload failed:", e)

# Usage
bucket_name = "etl-sbucket1"
destination_blob_name = "employee_data_fake_pii.csv"
upload_df_to_gcs(df, bucket_name, destination_blob_name)
