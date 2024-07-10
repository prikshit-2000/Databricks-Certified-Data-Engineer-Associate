# Databricks notebook source
spark

# COMMAND ----------

# MAGIC %md
# MAGIC # Title

# COMMAND ----------

# MAGIC %sql
# MAGIC select "Hello from Me"

# COMMAND ----------

# MAGIC %run ./Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls 'databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets/')
display(files)

# COMMAND ----------


