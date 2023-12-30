#include <WiFi.h>
#include <WiFiAP.h>

#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>


const char *ssid = "SlotMeasurements";
const char *password = "4data&speed";
const char *ip = "192.168.4.2";
const int port = 8888;

WiFiUDP udp;
Adafruit_BNO055 bno = Adafruit_BNO055(55);

sensors_event_t event;


void setup() {
  Serial.begin(115200);
  
  WiFi.softAP(ssid, password);

  if(!bno.begin())
  {
    Serial.print("No BNO055 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }
  
  delay(1000);
      
  bno.setExtCrystalUse(true);

  udp.begin(port);
}

void loop() {
  bno.getEvent(&event);
  udp.beginPacket(ip, port);
  float yaw = event.orientation.x;
  udp.print(String(millis()) + "," + String(event.orientation.x) + "," + String(event.orientation.y) + "," + String(event.orientation.z));
  udp.endPacket();
  delay(10);
}
