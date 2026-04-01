
void setup() {
  Serial.begin(9600);
}

void loop() {
  int altitude = random(100,500);
  int temperature = random(20,40);
  int battery = random(50,100);

  Serial.print(altitude);
  Serial.print(",");
  Serial.print(temperature);
  Serial.print(",");
  Serial.println(battery);

  delay(2000);
}
