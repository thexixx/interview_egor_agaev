from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder \
    .appName("PySpark Test") \
    .master("local[*]") \
    .getOrCreate()

# Create a small test DataFrame
data = [
    ("Alice", 25, "Engineer"),
    ("Bob", 30, "Data Scientist"),
    ("Charlie", 35, "Manager"),
    ("Diana", 28, "Analyst")
]

columns = ["Name", "Age", "Role"]

df = spark.createDataFrame(data, columns)

# Show the DataFrame
print("Test DataFrame:")
df.show()

# Print schema
print("\nDataFrame Schema:")
df.printSchema()

# Stop the Spark session
spark.stop()
