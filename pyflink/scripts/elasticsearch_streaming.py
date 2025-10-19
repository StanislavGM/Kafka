from pyflink.table import TableEnvironment, EnvironmentSettings

# Create a TableEnvironment
env_settings = EnvironmentSettings.in_streaming_mode()
t_env = TableEnvironment.create(env_settings)

# Specify connector and format jars
#t_env.get_config().get_configuration().set_string(
#    "pipeline.jars",
#    "file://home/cloud_user/kafka-3/py-hadoop-flink/flink/connectors/flink-sql-connector-kafka-4.0.0-2.0.jar",
#    "file://home/cloud_user/kafka-3/py-hadoop-flink/flink/connectors/flink-connector-elasticsearch8-4.0.0-2.0.jar",
#)

# Define source table DDL
source_table = """
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
          'topic' = 'elasticsearch-test-topic',
          'properties.bootstrap.servers' = 'kafka1:9092, kafka2:9092, kafka3:9092',
          'properties.group.id' = 'elasticsearch_group_id',
          'scan.startup.mode' = 'latest-offset',
          'format' = 'json'
    )
"""

# Define sink table DDL
sink_ddl = """
    CREATE TABLE sink_table(
        id_str VARCHAR,
        username VARCHAR,
        tweet VARCHAR,
        location VARCHAR,
        retweet_count BIGINT,
        followers_count BIGINT,
        lang VARCHAR
    ) WITH (
        'connector' = 'elasticsearch-7',
        'index' = 'kafka-flink-elastic-index',
        'hosts' = 'https://172.31.31.246:9200, https://172.31.31.82:9200',
        'format' = 'json'
    )
"""

# Execute DDL statements to create tables
t_env.execute_sql(source_ddl)
t_env.execute_sql(sink_ddl)

# Retrieve the source table
source_table = t_env.from_path('source_table')

print("Source Table Schema:")
source_table.print_schema()

# Process the data
result_table = source_table.select("*")

# Retrieve the sink table
sink_table = t_env.from_path('sink_table')

print("Sink Table Schema:")
sink_table.print_schema()

# Insert the processed data into the sink table
result_table.execute_insert('sink_table').wait()
