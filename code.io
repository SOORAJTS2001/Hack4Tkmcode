//FirebaseESP8266.h must be included before ESP8266WiFi.h
#include "FirebaseESP8266.h"  // Install Firebase ESP8266 library
#include <ESP8266WiFi.h>
int led = D4;
String data;
#define FIREBASE_HOST "nodemcu-fb649-default-rtdb.firebaseio.com/" //Without http:// or https:// schemes
#define FIREBASE_AUTH "2r07MVkdKLF9jaJdhDzPiygIiXde8hT5AQjWNBp7"
#define WIFI_SSID "SOORAJY91"
#define WIFI_PASSWORD "soorajsivadas767"

const int analogInPin = A0;
int sensorValue = 0;
//Define FirebaseESP8266 data object
FirebaseData firebaseData;
FirebaseData CutData;
FirebaseJson json;


void setup()
{

  Serial.begin(115200);
  pinMode(led, OUTPUT);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(300);
  }
  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.print(WiFi.localIP());
  Serial.println();

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.reconnectWiFi(true);

}

void sensorUpdate(int vVal, int cVal) {
  if (Firebase.setInt(firebaseData, "115206/Voltage", vVal))
  {
    Serial.println("PASSED VOLTAGE");
    /*Serial.println("PATH: " + firebaseData.dataPath());
      Serial.println("TYPE: " + firebaseData.dataType());
      Serial.println("ETag: " + firebaseData.ETag());
      Serial.println("------------------------------------");
      Serial.println();*/
  }
  else
  {
    Serial.println("FAILED");
    Serial.println("REASON: " + firebaseData.errorReason());
    Serial.println("------------------------------------");
    Serial.println();
  }
  Serial.print("\n");
  if (Firebase.setInt(firebaseData, "115206/Current", cVal))
  {
    Serial.println("PASSED CURRENT");
    /*Serial.println("PATH: " + firebaseData.dataPath());
      Serial.println("TYPE: " + firebaseData.dataType());
      Serial.println("ETag: " + firebaseData.ETag());
      Serial.println("------------------------------------");
      Serial.println();*/
  }
  else
  {
    Serial.println("FAILED");
    Serial.println("REASON: " + firebaseData.errorReason());
    Serial.println("------------------------------------");
    Serial.println();
  }
  Serial.print("\n");
}
void loop() {
  // read the analog in value
  sensorValue = analogRead(analogInPin);
  int voltage = map(sensorValue, 0, 1024, 0, 240);
  int current = voltage / 80;
  Serial.print("\n");
  Serial.print("voltage :");
  Serial.print(voltage);
  Serial.print("\n");
  Serial.print("current :");
  Serial.print(current);
  Serial.print("\n");
  // print the readings in the Serial Monitor
  sensorUpdate(voltage, current);
  if (Firebase.get(CutData, "115206/Cut"))
  {
    Serial.print(CutData.stringData());
    Serial.print("For Cutoff");
    data = CutData.stringData();
    Serial.print("\n");
    Serial.print("<------end of a cycle------>");
    if (data == "True")
    {
      Serial.println(CutData.stringData());
      digitalWrite(led, HIGH);
      delay(1000);
    }
    else if (data == "False")
    {
      Serial.println(CutData.stringData());
      digitalWrite(led, LOW);
      delay(1000);
    }
  }
  delay(1000);
}
