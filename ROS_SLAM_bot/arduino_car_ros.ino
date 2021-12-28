#if (ARDUINO >= 100)
#include <Arduino.h>
#else
#include <WProgram.h>
#endif
#include <ros.h>
#include <geometry_msgs/Twist.h>
// Pin variables for motors.
const int right_pwm_pin = 10;
const int right_fwd = 7;
const int right_dir_pin = 8;
const int left_pwm_pin = 11;
const int left_fwd = 12;
const int left_dir_pin = 13;



// Default_speed.
const int default_vel = 135;

ros::NodeHandle  nh;

void MoveFwd(const size_t speed) {
    digitalWrite(right_fwd,HIGH);
  digitalWrite(left_fwd,HIGH);
  digitalWrite(right_dir_pin, LOW);
  digitalWrite(left_dir_pin, LOW);
  analogWrite(right_pwm_pin, speed);
  analogWrite(left_pwm_pin, speed);
  
}

void MoveBack(const size_t speed) {
    digitalWrite(right_fwd,LOW);
  digitalWrite(left_fwd,LOW);
  digitalWrite(right_dir_pin, HIGH);
  digitalWrite(left_dir_pin, HIGH);
  analogWrite(right_pwm_pin, speed);
  analogWrite(left_pwm_pin, speed);
  
}
void MoveLeft(const size_t speed) {
  digitalWrite(right_fwd,HIGH);
  digitalWrite(right_dir_pin, LOW);
  digitalWrite(left_fwd,LOW);
   digitalWrite(left_dir_pin, HIGH);
  analogWrite(right_pwm_pin, speed+100);
  analogWrite(left_pwm_pin, speed+100);
  
}
void MoveRight(const size_t speed) {
  digitalWrite(right_fwd,LOW);
  digitalWrite(right_dir_pin, HIGH);
  digitalWrite(left_fwd,HIGH);
  digitalWrite(left_dir_pin, LOW);
  analogWrite(right_pwm_pin, speed);
   analogWrite(left_pwm_pin, speed);
  
}

void MoveStop() {
  digitalWrite(left_fwd, LOW);
  digitalWrite(left_dir_pin, LOW);
  digitalWrite(right_fwd, LOW);
  digitalWrite(right_dir_pin, LOW);
  analogWrite(left_pwm_pin, LOW);
  analogWrite(right_pwm_pin, LOW);
}

void cmd_vel_cb(const geometry_msgs::Twist & msg) {
  // Read the message. Act accordingly.
  // We only care about the linear x, and the rotational z.
  const float x = msg.linear.x;
  const float z_rotation = msg.angular.z;

  // Decide on the morot state we need, according to command.
  if (x > 0 && z_rotation == 0) {
    MoveFwd(default_vel);
  }
  else if(x == 0 && z_rotation > 0){
   
    MoveLeft(default_vel);
  }else if(x == 0 && z_rotation < 0){

    MoveRight(default_vel);
  }else if(x < 0 && z_rotation == 0){
    MoveBack(default_vel);
  }else{
    MoveStop();
  }
}
ros::Subscriber<geometry_msgs::Twist> sub("cmd_vel", cmd_vel_cb);
void setup() {
  pinMode(right_pwm_pin, OUTPUT);    // sets the digital pin 13 as output
  pinMode(right_dir_pin, OUTPUT);
  pinMode(left_pwm_pin, OUTPUT);
  pinMode(left_dir_pin, OUTPUT);
  pinMode(right_fwd, OUTPUT);
  pinMode(left_fwd, OUTPUT);


  nh.initNode();
  nh.subscribe(sub);
}

void loop() {
  nh.spinOnce();
  delay(1);
}
