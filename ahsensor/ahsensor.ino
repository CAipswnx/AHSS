#include <SimpleDHT.h>
#include <Wire.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include "music.h"

//pin
#define SoundSensorPin 36 
#define pinDHT11 23

//values
#define VREF 5.0
String sensor_name = "ahss_1";
String sensor_type = "allSensor";
int detectHuman = 0;
String resultMusic = "";

//DHT11
SimpleDHT11 dht11(pinDHT11);

//WIFI連線
char SSID[] = "caa";
char PASSWORD[] = "00002222";

//計算時間
long sendTime = 0;
long detectHumanTime = 0;

void setup() 
{
  Serial.begin(115200);
  pinMode(SoundSensorPin,OUTPUT); //聲音感測器
  pinMode(16,INPUT);  //人體紅外線
  pinMode(17,OUTPUT); //播放錄音
  WifiConnect();      //WIFI連線
}
void loop() {
  byte temperature = 0;
  byte humidity = 0;
  if(sendTime == 0 || millis() - sendTime >= 15000){
    ReadDHT(&temperature, &humidity);            //讀取溫溼度
    float dBValue = ReaddBA();                     //讀取分貝
    sendData(&temperature, &humidity, dBValue); //送出資料
  }
  if(detectHumanTime ==0 || millis() - detectHumanTime >= 15000 ){
    comingWarn(); //人體感測
    detectHumanTime = millis();
  }
  if(resultMusic != ""){
    if(resultMusic == "bbq"){
      Serial.print("播放BBQ");
      bbq();
    }else if(resultMusic == "twomin"){
      twomin();
    }else if(resultMusic == "canon"){
      canon();
    }
  }

}

//連線WIFI
void WifiConnect() {
  Serial.print("Connecting Wifi: ");
  Serial.println(SSID);
  WiFi.begin(SSID, PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  //連線成功，顯示取得的IP
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  IPAddress ip = WiFi.localIP();
  Serial.println(ip);
}

//讀取DHT11溫濕度
void ReadDHT(byte *temperature, byte *humidity) {
  int err = SimpleDHTErrSuccess;
  if ((err = dht11.read(temperature, humidity, NULL)) !=
      SimpleDHTErrSuccess) {
    Serial.print("讀取失敗,錯誤訊息=");
    Serial.print(SimpleDHTErrCode(err));
    Serial.print(","); Serial.println(SimpleDHTErrDuration(err));
    delay(1000);
    return;
  }
  Serial.print("DHT讀取成功：");
  Serial.print((int)*temperature); Serial.print(" *C, ");
  Serial.print((int)*humidity); Serial.println(" H");
}

float ReaddBA(){
  float voltageValue, dBValue;
  voltageValue = analogRead(SoundSensorPin) / 1024.0 * VREF;
  dBValue = voltageValue * 95.377;  
  Serial.print(dBValue, 1);
  Serial.println(" dBA");
  return dBValue;
}

void comingWarn(){
  if(digitalRead(16) == HIGH && detectHuman == 0){
    Serial.println("Coming");
    digitalWrite(17,HIGH);
    detectHuman = 1;
  }
  else{
    Serial.println("None");
    digitalWrite(17,LOW);
    detectHuman = 0;
  }
}

//傳送資料
void sendData(byte *temperature, byte *humidity, float dBValue) {

  HTTPClient http;
  //post方式
  http.begin("http://34.173.184.110:5000/sensor/addData"); //傳送位址
  http.addHeader("Content-Type", "application/x-www-form-urlencoded"); //傳送格式
  String httpRequestData = "sensor_name=" + sensor_name + "&sensor_type=" + sensor_type + "&temperature=" + String(((int)*temperature)) + "&humidity=" + String(((int)*humidity)) + "&dba=" + String(dBValue); //資料傳送
  int httpCode = http.POST(httpRequestData); //使用POST方式
  
  //get方式
  //http.begin("3.86.60.99",5000,"/test?test=abc"); //傳送位址
  //const char *headerKeys[] = {"Content-Type","Content-Length"};
  //http.collectHeaders(headerKeys,2);
  //int httpCode = http.GET(); //使用GET方式
  
  if(httpCode == HTTP_CODE_OK)
  {
    
    String resultData = http.getString();//資料接收
    Serial.println(resultData); 
    int starts = 0;
    int ends = resultData.indexOf("=");
    String key = resultData.substring(0,ends);
    String value ="";
    
    if(key=="music")
    {
      starts = ends;
      ends = resultData.indexOf("&");
      if(ends == -1)
      {
        value = resultData.substring(starts+1);
      } else
      {
        value = resultData.substring(starts+1,ends);
      }
      resultMusic = value;
      starts = ends;
      resultData = resultData.substring(starts+1);
      
    }
    
  }
  else
  {
    Serial.println(http.errorToString(httpCode)); //錯誤訊息
  }
  http.end();
  sendTime = millis();
}
  
