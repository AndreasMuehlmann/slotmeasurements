#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiAP.h>

#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

const char *ssid = "SlotMeasurements";
const char *password = "4data&speed";


WiFiServer server(8888);
Adafruit_BNO055 bno = Adafruit_BNO055(55);
sensors_event_t event;

void setup() {
  Serial.begin(115200);
  
  WiFi.softAP(ssid, password);

  if(!bno.begin())
  {
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }
  
  delay(1000);
      
  bno.setExtCrystalUse(true);

  Serial.println("ESP32-P2P Server");
  Serial.print("IP Address: ");
  Serial.println(WiFi.softAPIP());

  server.begin();
}

void loop() {
  WiFiClient client = server.available();

  if (client) {
    Serial.println("New client connected");
    unsigned int start = millis();
    while (client.connected()) {
      bno.getEvent(&event);
      if (client.available()) {
        String data = client.readStringUntil('\n');
        client.println(String(millis()) + "," + String(event.orientation.x) + "," + String(event.orientation.y) + "," + String(event.orientation.z));
      }
      delay(10);
      Serial.println(String(millis() - start));
      start = millis();
    }
    

    Serial.println("Client disconnected");
    client.stop();
  }
  delay(100);
}