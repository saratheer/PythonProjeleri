import random

def upgrade(mevcutSeviye, maxUpgradeLvl):
  for i in range(maxUpgradeLvl):
    sansFaktörü = random.uniform(0, 1)
    # Şans faktörünü hesaplayın
    zorlukSansSeviyesi = 1 - (i / maxUpgradeLvl)
    if sansFaktörü > zorlukSansSeviyesi:
      mevcutSeviye += 1
  return mevcutSeviye

# Örnek kullanım
mevcutSeviye = 1
maxUpgradeLvl = 9
son_level = upgrade(mevcutSeviye, maxUpgradeLvl)
print(f"Yükseltme işlemi sonucu nesnenin seviyesi:{son_level}")
