from pyflink.table import TableEnvironment, EnvironmentSettings

# Create a TableEnvironment
env_settings = EnvironmentSettings.in_streaming_mode()
t_env = TableEnvironment.create(env_settings)

# Specify connector and format jars
t_env.get_config().get_configuration().set_string(
    "pipeline.jars",
#    "file:///home/cloud_user/kafka-3/pyflink/flink-sql-connector-kafka-3.4.0-1.20.jar"
    "file:///home/cloud_user/kafka-3/pyflink/flink-sql-connector-kafka-4.0.0-2.0.jar"
)

# Define source table DDL
source_ddl = """
    CREATE TABLE source_table(
        id_str VARCHAR,
        username VARCHAR,
        tweet VARCHAR,
        location VARCHAR,
        retweet_count BIGINT,
        followers_count BIGINT,
        lang VARCHAR
    ) WITH (
        'connector' = 'kafka',
        'topic' = 'stream-twitter-events',
        'properties.bootstrap.servers' = 'kafka1:9092,kafka2:9092,kafka3:9092',
        'properties.group.id' = 'flink_sql_cons_group_id',
        'scan.startup.mode' = 'earliest-offset',
        'format' = 'json'
    )
"""

# Execute DDL statement to create the source table
t_env.execute_sql(source_ddl)

# Retrieve the source table
source_table = t_env.from_path('source_table')

print("Source Table Schema:")
source_table.print_schema()

# Define a SQL query to select all columns from the source table
sql_query = "SELECT * FROM source_table"

# Execute the query and retrieve the result table
result_table = t_env.sql_query(sql_query)

# Print the result table to the console
result_table.execute().print()
