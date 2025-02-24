import pandas as pd
import numpy as np
from faker import Faker

faker = Faker()

def generate_fake_users(num=50, seed=None): # adjust num value to required number of records
    np.random.seed(seed)
    faker.seed_instance(seed)

    users = []
    domain = "studentemail.edu"  # Replace with your desired email domain

    for _ in range(num):
        gender = np.random.choice(["M", "F"], p=[0.5, 0.5])  # Adjust gender ratios as needed
        first_name = faker.first_name_male() if gender == "M" else faker.first_name_female()
        last_name = faker.last_name()
        user_id = np.random.randint(1000000000, 9999999999)  # Generate a unique 10-digit identifier
        email = f"{first_name.lower()}.{last_name.lower()}@{domain}"

        users.append({
            "First Name": first_name,
            "Last Name": last_name,
            "Email": email,
            "User ID": user_id
        })

    return users

# Generate and save the data to CSV
df = pd.DataFrame(generate_fake_users(num=50, seed=42))
csv_filename = "fake_users.csv"
df.to_csv(csv_filename, index=False)

print(f"CSV file saved: {csv_filename}")
