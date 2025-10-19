package wikimedia;

import okhttp3.Headers;
import com.launchdarkly.eventsource.EventHandler;
import com.launchdarkly.eventsource.EventSource;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.common.serialization.StringSerializer;

import java.net.URI;
import java.util.Properties;
import java.util.concurrent.TimeUnit;

public class WikimediaChangesProducer {
    public static void main(String[] args) throws InterruptedException {
	// Create the Producer Properties
	Properties properties = new Properties();
	properties.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "kafka1:9092,kafka2:9092,kafka3:9092");
	properties.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
	properties.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());

	//Create Producer
	KafkaProducer<String, String> producer = new KafkaProducer<>(properties);
	String topic = "wikimedia.recent.change";
	EventHandler eventHandler = new WikimediaChangeHandler(producer, topic);
	String url = "https://stream.wikimedia.org/v2/stream/recentchange";
//	EventSource.Builder builder = new EventSource.Builder(eventHandler, URI.create(url));
	Headers headers = new Headers.Builder().add("User-Agent", "Gradle").build();
	EventSource.Builder builder = new EventSource.Builder(eventHandler, URI.create(url)).headers(headers);
	EventSource eventSource = builder.build();

	//Start the Producer in another thread
	eventSource.start();
	
	//We produce for 5 minutes and block the program until then
	TimeUnit.MINUTES.sleep(5);
    }
}
