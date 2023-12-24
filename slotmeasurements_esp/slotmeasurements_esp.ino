#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiAP.h>

const char *ssid = "SlotMeasurements";
const char *password = "4data&speed"; // Change this to a secure password

WiFiServer server(8888);

void setup() {
  Serial.begin(115200);
  

  // Connect to WiFi network
  WiFi.softAP(ssid, password);

  delay(1000);
  Serial.println("ESP32-P2P Server");
  Serial.print("IP Address: ");
  Serial.println(WiFi.softAPIP());

  server.begin();
}

void loop() {
  WiFiClient client = server.available();

  if (client) {
    Serial.println("New client connected");

    while (client.connected()) {
      if (client.available()) {
        String data = client.readStringUntil('\n');
        client.println("1, 2, 3");
      }
    }

    Serial.println("Client disconnected");
    client.stop();
  }
}