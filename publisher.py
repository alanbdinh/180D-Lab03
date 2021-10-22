import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connection returned result: "+str(rc))
	for i in range(10):
		client.publish(topic = 'aland', payload = i, qos=1)
		print('pub loop #' + str(i) + '\n')
	#client.disconnect()
# Subscribing in on_connect() means that if we lose the connection and
# reconnect then subscriptions will be renewed.

def on_disconnect(client, userdata, rc):
	if rc != 0:
		print('Unexpected Disconnect')
	else:
		print('Expected Disconnect')
# The default message callback.
# (won’t be used if only publishing, but can still exist)
def on_publish(client, userdata, mid):
	print('Published message with ID %i' % mid)

client = mqtt.Client()

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

client.connect('mqtt.eclipseprojects.io', 1883, 5)
client.loop_forever()