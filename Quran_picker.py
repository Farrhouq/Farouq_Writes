#For picking random verses for Muraaja'ah(for Quran memorisers).
import pyquran as pq
import random

theQuran = {}
for num in range(114):
    theQuran[str(num)] = pq.quran.get_sura(num, with_tashkeel=True)
    
sura_numbers = [key for key in theQuran]

selected_sura_number = random.choices(sura_numbers)
sura_name = pq.quran.get_sura_name(int(selected_sura_number[0]))
 
selected_sura = pq.quran.get_sura(int(selected_sura_number[0]), with_tashkeel = True) 
print(random.choices(selected_sura))
