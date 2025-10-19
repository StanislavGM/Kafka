wget https://dlcdn.apache.org/kafka/3.9.1/kafka_2.13-3.9.1.tgz
wget https://dlcdn.apache.org/zookeeper/zookeeper-3.9.3/apache-zookeeper-3.9.3-bin.tar.gz
gunzip kafka_2.13-3.9.1.tgz && tar -xf kafka_2.13-3.9.1.tar && mv kafka_2.13-3.9.1 kafka && rm -f kafka_2.13-3.9.1.tar
gunzip apache-zookeeper-3.9.3-bin.tar.gz && tar -xf apache-zookeeper-3.9.3-bin.tar && mv apache-zookeeper-3.9.3-bin zookeeper && rm -f apache-zookeeper-3.9.3-bin.tar
