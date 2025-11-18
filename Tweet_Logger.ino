int sensorPin = A0;

void setup() {
  Serial.begin(9600); 
}

void loop() {
  int analogValue = analogRead(sensorPin);
  float voltage = analogValue * (5.0 / 1023.0);
  float temperature = (voltage * 100.0) / 4.0; // LM35 formula

  Serial.println(temperature);  
  delay(10000); 
}
