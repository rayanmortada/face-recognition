from deepface import DeepFace
import pyodbc

# Specify the paths
db_path = r'C:\Users\admin\OneDrive\Desktop\my-db'
image_path = r'C:\Users\admin\OneDrive\Desktop\image4.jpeg'

# Use DeepFace to find the image in the database
dfs = DeepFace.find(img_path=image_path, db_path=db_path)


# If there is a match, extract the path from the 'identity' column of the first DataFrame
if dfs:
    first_df = dfs[0]
    found_path = first_df['identity'].iloc[0]
    print(f"Extracted Path: {found_path}")
else:
    print("No matches found in the database for the provided image.")



# Connect to your database

server_name = "DESKTOP-15KBTQ3"
database_name = "Gym-Project"
connection_string = f'DRIVER={{SQL Server}};SERVER={server_name};DATABASE={database_name};Trusted_Connection=yes;'
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# Query the database to find the userId related to the extracted path
query = "SELECT userID,Fname FROM users WHERE imgPath = ?"
cursor.execute(query, str(found_path))
result = cursor.fetchone()

# Check if a userId was found
if result:
        user_id = result[0]
        name = result[1]

        print(f"User ID: {user_id} , name:{name}")
else:
        print("User ID not found for the extracted image path.")

