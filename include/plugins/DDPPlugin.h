#pragma once

#include "PluginManager.h"
#ifdef ESP32
#include "AsyncUDP.h"
#else
#include "ESPAsyncUDP.h"
#endif
class DDPPlugin : public Plugin
{
private:
  AsyncUDP *udp;

public:
  void setup() override;
  void teardown() override;
  void loop() override;
  const char *getName() const override;
};
