cmake_minimum_required(VERSION 3.5)

#https://espressif-docs.readthedocs-hosted.com/projects/arduino-esp32/en/latest/esp-idf_component.html

idf_component_register(SRCS "AsyncElegantOTA.cpp"
                       INCLUDE_DIRS "."
                       PRIV_REQUIRES driver arduino-esp32 AsyncTCP ESPAsyncWebServer)
