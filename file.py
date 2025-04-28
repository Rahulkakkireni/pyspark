pip install pyspark
df=spark.read.csv('annual.csv')

df.printSchema()
