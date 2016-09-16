int a = 0, b = 0, c = 0, d = 0;
int val = 0;
int PWM_Motor1 = 3;
int PWM_Motor2 = 9;

void setup()
{
  Serial.begin(9600);
  // Operation Code
  pinMode(6,INPUT);
  pinMode(7,INPUT);
  pinMode(12,INPUT);
  pinMode(13,INPUT);
  
  // Motor 1
  pinMode(2,OUTPUT);
  pinMode(PWM_Motor1,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  
  // Motor 2
  pinMode(8,OUTPUT);
  pinMode(PWM_Motor2,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
}

void loop()
{
  if(a==0 & b==0 & c==0 & d==1)    // Speed UP
  {
    val = 255;
    analogWrite(PWM_Motor1,val);
    analogWrite(PWM_Motor2,val);
  }
  else if(a==0 & b==0 & c==1 & d==0)    // Forward
  {
    digitalWrite(2,1);
    digitalWrite(8,1);
    digitalWrite(4,1);
    digitalWrite(5,0);
    digitalWrite(10,1);
    digitalWrite(11,0);
    analogWrite(PWM_Motor1,185);
    analogWrite(PWM_Motor2,185);
  }
  else if(a==0 & b==0 & c==1 & d==1)    // Speed Down
  {
    val = 125;
    analogWrite(PWM_Motor1,val);
    analogWrite(PWM_Motor2,val);
  }
  else if(a==0 & b==1 & c==0 & d==0)    // Left
  {
    analogWrite(PWM_Motor1,155);
    analogWrite(PWM_Motor2,155);
    digitalWrite(2,1);
    digitalWrite(8,1);
    digitalWrite(4,0);
    digitalWrite(5,1);
    digitalWrite(10,1);
    digitalWrite(11,0);    
  }
  else if(a==0 & b==1 & c==0 & d==1)    // Stop
  {
    digitalWrite(2,0);
    digitalWrite(8,0);
    analogWrite(PWM_Motor1,0);
    analogWrite(PWM_Motor2,0);
  }
  else if(a==0 & b==1 & c==1 & d==0)    // Right
  {
    analogWrite(PWM_Motor1,155);
    analogWrite(PWM_Motor2,155);
    digitalWrite(2,1);
    digitalWrite(8,1);
    digitalWrite(4,1);
    digitalWrite(5,0);
    digitalWrite(10,0);
    digitalWrite(11,1);
  }
  else if(a==1 & b==0 & c==0 & d==0)    // Backward
  {
    digitalWrite(2,1);
    digitalWrite(8,1);
    digitalWrite(4,0);
    digitalWrite(5,1);
    digitalWrite(10,0);
    digitalWrite(11,1);
    analogWrite(PWM_Motor1,185);
    analogWrite(PWM_Motor2,185);
  }
}
