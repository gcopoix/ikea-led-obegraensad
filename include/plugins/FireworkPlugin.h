#pragma once

#include "PluginManager.h"

class FireworkPlugin : public Plugin
{
private:
  unsigned long previousMillis = 0;
  const unsigned int explosionDelay = 60;
  const unsigned int fadeDelay = 24;
  const unsigned int rocketDelay = 60;
  const unsigned int explosionDuration = 500;

  void drawExplosion(int x, int y, int maxRadius, int brightness);
  void explode(int x, int y);

public:
  void setup() override;
  void loop() override;
  const char *getName() const override;
};
