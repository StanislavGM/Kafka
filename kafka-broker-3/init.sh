list=("zookeeper3" "kafka3" "docker")
for service in "${list[@]}";
do
  sudo service $service start
  sleep 1
done
####
# provectuslabs/kafka-ui:latest
# landoop/kafka-topics-ui:0.9.4
# confluentinc/cp-kafka-rest:7.2.15
# confluentinc/cp-schema-registry:7.2.15
