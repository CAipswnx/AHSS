#include <ESP32Servo.h>
int Do=262;
int hDo_=1109;
int re=294;
int hre_=1245;
int mi=330;
int hmi=1318;
int fa=349;
int hfa_=1480;
int so=392;
int hso_=1661;
int ra=440;
int hra=1760;
int si=493;
int buzzer= 18;

void bbq() {
  tone(buzzer, so, 250);
  tone(buzzer, so, 250);
  tone(buzzer, so, 250);
  tone(buzzer, so, 250);
  tone(buzzer, so, 250);
  tone(buzzer, so, 250);
  delay(100);
  tone(buzzer, ra, 250);
  tone(buzzer, so, 250);
  tone(buzzer, ra, 400);
  tone(buzzer, so, 400); 
  delay(300);
  tone(buzzer, ra, 250);
  tone(buzzer, so, 250);
  tone(buzzer, ra, 250);
  tone(buzzer, so, 250);
  tone(buzzer, ra, 400);
  tone(buzzer, so, 400);
  delay(100);
  tone(buzzer, re, 250);
  tone(buzzer, mi, 250); 
  tone(buzzer, re, 250);
  tone(buzzer, Do, 250);
  tone(buzzer, re, 400);
  delay(300);
  tone(buzzer, so, 250); 
  tone(buzzer, so, 250);
  tone(buzzer, so, 250);
  tone(buzzer, ra, 250);
  tone(buzzer, so, 400);
   delay(300);
  tone(buzzer, re, 250);
  tone(buzzer, re, 250);
  tone(buzzer, re, 250);
  tone(buzzer, mi, 250);
  tone(buzzer, re, 400);
    delay(300);
  tone(buzzer, re, 250);
  tone(buzzer, Do, 250);
  tone(buzzer, re, 250);
  tone(buzzer, mi, 250);
  tone(buzzer, re, 400);
  tone(buzzer, re, 400);
   delay(300);
   tone(buzzer, re, 250);
   tone(buzzer, mi, 250);
   tone(buzzer, re, 400);
   tone(buzzer, Do, 400);
}

void canon() {
  tone(buzzer, 1568, 400);
  tone(buzzer, 1318, 250);
  tone(buzzer, 1397, 250);
  tone(buzzer, 1568, 400);
  delay(100);
  tone(buzzer, 1318, 250);
  tone(buzzer, 1397, 250);
  tone(buzzer, 1568, 250);
  tone(buzzer, so, 250);
  tone(buzzer, ra, 250);
  tone(buzzer, si, 250);
  tone(buzzer, 1047, 250);
  tone(buzzer, 1175, 250);
  tone(buzzer, 1318, 250);
  tone(buzzer, 1397, 250);
  tone(buzzer, 1318, 400);
  tone(buzzer, 1047, 250);
  tone(buzzer, 1175, 250);
  tone(buzzer, 1318, 400);
  tone(buzzer, mi, 250);
  tone(buzzer, fa, 250); 
  tone(buzzer, so, 250);
  tone(buzzer, ra, 250);
  tone(buzzer, so, 250);
  tone(buzzer, fa, 250); 
  tone(buzzer, so, 250);
  tone(buzzer, 1047, 250);
  tone(buzzer, si, 250);
  tone(buzzer, 1047, 250);
  tone(buzzer, ra, 400);
  tone(buzzer, 1047, 250);
  tone(buzzer, si, 250);
  tone(buzzer, ra, 400);
  tone(buzzer, so, 250);
  tone(buzzer, fa, 250);
  tone(buzzer, so, 250);
  tone(buzzer, fa, 250);
  tone(buzzer, mi, 250);
  tone(buzzer, fa, 250);
  tone(buzzer, so, 250);
  tone(buzzer, ra, 250);
  tone(buzzer, si, 250);
  tone(buzzer, 1047, 250);
  tone(buzzer, ra, 400);
  tone(buzzer, 1047, 250);
  tone(buzzer, si, 250);
  tone(buzzer, 1047, 400);
  tone(buzzer, si, 250);
  tone(buzzer, 1047, 250);
  tone(buzzer, si, 250);
  tone(buzzer, ra, 250);
  tone(buzzer, si, 250);
  tone(buzzer, 1047, 250);
  tone(buzzer, 1175, 250);
  tone(buzzer, 1318, 250);
  tone(buzzer, 1397, 250);
  tone(buzzer, 1568, 250);
  tone(buzzer, 1568, 400);
   tone(buzzer, 1318, 250);
  tone(buzzer, 1397, 250);
  tone(buzzer, 1568, 250);
  delay(100);
  tone(buzzer, 1318, 250);
  tone(buzzer, 1397, 250);
  tone(buzzer, 1568, 250);
  tone(buzzer, so, 250);
  tone(buzzer, ra, 250);
  tone(buzzer, si, 250);
  tone(buzzer, 1047, 250);
  tone(buzzer, 1175, 250);
  tone(buzzer, 1318, 250);
  tone(buzzer, 1397, 250);
  tone(buzzer, 1318, 400);
  tone(buzzer, 1047, 250);
  tone(buzzer, 1175, 250);
  tone(buzzer, 1318, 400);
  tone(buzzer, mi, 250);
  tone(buzzer, fa, 250);
  tone(buzzer, so, 250);
  tone(buzzer, ra, 250);
  tone(buzzer, so, 250);
  tone(buzzer, fa, 250);
  tone(buzzer, so, 250);
  tone(buzzer, 1047, 250);
  tone(buzzer, si, 250);
  tone(buzzer, 1047, 250);
  tone(buzzer, ra, 400);
  tone(buzzer, 1047, 250);
  tone(buzzer, si, 250);
  tone(buzzer, ra, 400);
  tone(buzzer, so, 250);
  tone(buzzer, fa, 250);
  tone(buzzer, so, 250);
  tone(buzzer, fa, 250);  
  tone(buzzer, mi, 250);
  tone(buzzer, fa, 250);
  tone(buzzer, so, 250);
  tone(buzzer, ra, 250);
  tone(buzzer, si, 250);
  tone(buzzer, 1047, 250);
  tone(buzzer, ra, 400);
  tone(buzzer, 1047, 250);
  tone(buzzer, si, 250);
  tone(buzzer, 1047, 400);
  tone(buzzer, si, 250);
  tone(buzzer, ra, 250);
  tone(buzzer, si, 250);
  tone(buzzer, 1047, 250);
  tone(buzzer, 1175, 250);
  tone(buzzer, 1047, 250);
  tone(buzzer, si, 250);
  tone(buzzer, 1047, 250);
  tone(buzzer, ra, 250);
  tone(buzzer, si, 250);
  tone(buzzer, 1047, 400);
}

void twomin() {
  tone(buzzer, hso_, 400);
  tone(buzzer, hfa_, 400);
  tone(buzzer, hmi, 400);
  tone(buzzer, hDo_, 400);
  tone(buzzer, hfa_, 250);
  tone(buzzer, hfa_, 400);
  delay(300);
  tone(buzzer, hso_, 400);
  tone(buzzer, hfa_, 400);
  tone(buzzer, hmi, 400);
  tone(buzzer, 988, 400);
  tone(buzzer, hfa_, 250);
  tone(buzzer, hfa_, 400);
  tone(buzzer, hmi, 250);
  tone(buzzer, hmi, 400);
  delay(300);
  tone(buzzer, hso_, 400);
  tone(buzzer, hfa_, 400);
  tone(buzzer, hmi, 400);
  tone(buzzer, hDo_, 400);
  tone(buzzer, hfa_, 250);
  tone(buzzer, hfa_, 400);
  tone(buzzer, hmi, 250);
  tone(buzzer, hra, 400);
  tone(buzzer, hso_, 250);
  tone(buzzer, hfa_, 400);
  tone(buzzer, hmi, 400);
  tone(buzzer, 988, 250);
  tone(buzzer, hra, 400);
  tone(buzzer, hso_, 250);
  tone(buzzer, hso_, 400);
  tone(buzzer, hfa_, 400);
  tone(buzzer, hso_, 400);
  delay(100);
  tone(buzzer, hso_, 250);
  tone(buzzer, hra, 400);
  tone(buzzer, 2217, 400);
  tone(buzzer, hso_, 250);
  tone(buzzer, hso_, 400);
  tone(buzzer, hfa_, 250);
  tone(buzzer, hfa_, 400);
  tone(buzzer, hfa_, 250);
  tone(buzzer, hso_, 400);
  tone(buzzer, hfa_, 250);
  tone(buzzer, 1976, 400);
  tone(buzzer, hfa_, 250);
  tone(buzzer, hfa_, 400);
  tone(buzzer, hre_, 250);
  tone(buzzer, hfa_, 400);
  tone(buzzer, hmi, 400);
  delay(100);
  tone(buzzer, 880, 400);
  tone(buzzer, 831, 400);
  tone(buzzer, 880, 400);
  tone(buzzer, hmi, 250);
  tone(buzzer, hmi, 400);
  tone(buzzer, hfa_, 425);
  tone(buzzer, hra, 400);
  tone(buzzer, hso_, 400); 
  tone(buzzer, hfa_, 400);
  tone(buzzer, hmi, 400); 
  tone(buzzer, hmi, 400); 
}
