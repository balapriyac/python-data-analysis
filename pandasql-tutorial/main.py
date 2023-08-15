# necessary imports
import pandas as pd
import seaborn as sns
from pandasql import sqldf


# Define a reusable function for running SQL queries
run_query = lambda query: sqldf(query, globals())

# Load the "tips" dataset into a Pandas DataFrame
tips_df = sns.load_dataset("tips")

# Simple select query
query1 = """
SELECT *
FROM tips_df
LIMIT 5;
"""
result1 = run_query(query1)
print(result1)

