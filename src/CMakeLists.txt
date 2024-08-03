FILE(GLOB MY_SRCS *.c *.cpp plugins/*.cpp)

#https://espressif-docs.readthedocs-hosted.com/projects/arduino-esp32/en/latest/esp-idf_component.html

idf_component_register(SRCS ${MY_SRCS}
                       INCLUDE_DIRS "${CMAKE_SOURCE_DIR}/include"
                       REQUIRES driver esp_wifi nvs_flash esp_http_server arduino-esp32 WiFiManager AsyncTCP AsyncElegantOTA ESPAsyncWebServer ArduinoJson)
