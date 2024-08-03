cmake_minimum_required(VERSION 3.5)

# dummy "arduino" forward component to satisfy dependencies (WiFiManager)
idf_component_register(REQUIRES arduino-esp32)
