int ir1 = A8;
int ir1_obst = HIGH;
int ir2 = A9;
int ir2_obst = HIGH;
int ir3 = A10;
int ir3_obst = HIGH;
int servo1 =51;
int servo2 =52;
int servo3 = 53;

void setup() {
  pinMode(servo1,OUTPUT);
  pinMode(ir1,INPUT);
  pinMode(servo2,OUTPUT);
  pinMode(ir2,INPUT);
  pinMode(servo3,OUTPUT);
  pinMode(ir3,INPUT);
  Serial.begin(9600);
 }

void loop() {
 ir1_obst = digitalRead(ir1);
  if (ir1_obst == LOW)
  {
    Serial.print("first grade obst detected");
    digitalWrite(servo1,HIGH);
    }
    else {
      Serial.print("first path is clear");
      digitalWrite(servo1,LOW);
      }
      delay(200);
      ir2_obst = digitalRead(ir2);
  if (ir2_obst == LOW && ir1_obst == LOW)
  {
    Serial.print("second grade obst detected");
    digitalWrite(servo2,HIGH);
    }
    else {
      Serial.print("second path is clear");
      digitalWrite(servo2,LOW);
      }
      delay(200);
      ir3_obst = digitalRead(ir3);
  if (ir3_obst == LOW && ir2_obst == LOW && ir1_obst ==LOW)
  {
    Serial.print("third grade obst detected");
    digitalWrite(servo3,HIGH);
    }
    else {
      Serial.print("third path is clear");
      digitalWrite(servo3,LOW);
      }
      delay(200);
      
      }
