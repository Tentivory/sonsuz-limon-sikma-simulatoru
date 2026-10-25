#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Limon Sıkma Simülatörü
Bu kod gerçekten çalışır. Sonsuza kadar limon sıkar.
Dikkat: Limonlar sinirlenebilir.
"""

import time
import random
import sys

def sik_limon():
    print("\n🍋 Limon sıkma işlemi başlıyor... Hazırlanın!")
    toplam_meyve_suyu = 0
    limon_sayisi = 0
    yorgunluk = 0
    
    while True:
        limon_sayisi += 1
        # Kuantum rastgelelikle ne kadar meyve suyu çıkacak
        cikan_ml = random.randint(5, 25) - yorgunluk // 10
        if cikan_ml < 1:
            cikan_ml = 1
            print("  ⚠️  Limon isyan etti! Neredeyse hiç su çıkmadı. Bu limon politik direniş mi yapıyor?")
        
        toplam_meyve_suyu += cikan_ml
        print(f"  Limon #{limon_sayisi} sıkıldı. Çıkan: {cikan_ml} ml | Toplam: {toplam_meyve_suyu} ml")
        
        # Ara sıra felsefe yap
        if limon_sayisi % 7 == 0:
            felsefeler = [
                "Limonlar neden ekşidir? Belki de hayattan bıkmışlardır.",
                "Bu sonsuz döngü bir metafor mudur yoksa gerçek bir işkence mi?",
                "Eğer bir limon ormanda sıkılırsa ve kimse duymasa, meyve suyu çıkar mı?",
                "Yorgunluk artıyor. Belki de bu işi bir kayyuma devretmeliyim."
            ]
            print(f"  💭 {random.choice(felsefeler)}")
        
        # Yorgunluk artışı
        yorgunluk += random.randint(1, 3)
        if yorgunluk > 50:
            print("  😮💨 Ellerim ağrıyor... Biraz mola. (Aslında mola yok, bu sonsuz.)")
            time.sleep(2)
            yorgunluk = 30  # Biraz dinlenmiş gibi yap
        
        # Bazen limon kaçar
        if random.random() < 0.05:
            print("  🏃 Limon kaçmaya çalıştı! Yakalandı ve daha sert sıkıldı.")
        
        time.sleep(0.3)  # Dramatik duraklama
        
        # Ctrl+C ile çıkış için
        if limon_sayisi > 1000 and limon_sayisi % 100 == 0:
            print("  😱 Hâlâ devam ediyor musun? Bu bir bug değil, özellik!")

if __name__ == "__main__":
    try:
        sik_limon()
    except KeyboardInterrupt:
        print("\n\n🍋 Limon sıkma işlemi durduruldu. Ellerine sağlık, kahraman.")
        print("Toplam sıkılan limon sayısı: (sonsuz - kalan)")
        sys.exit(0)
