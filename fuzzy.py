# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 03:52:45 2021

@author: rendi
"""
    
x_kinerja = int(input('Masukan kinerja : '))
x_kedisiplinan = int(input('Masukan kedisiplinan : '))
x_kemampuan = int(input('Masukan Kemampuan : '))


#rumus kinerja = (x - a) / (b-a)
# Kinerja
if (x_kinerja <= 60) :
   hasil_tdk_puas_kinerja = (x_kinerja - 60) / (80 - 60)
   hasil_puas_kinerja = 0
elif (x_kinerja > 60 and x_kinerja < 80) :
    hasil_tdk_puas_kinerja = (60 - x_kinerja) / (80 - 60)
    hasil_puas_kinerja = (x_kinerja - 80) / (80 - 60)
elif (x_kinerja >= 80) : 
    hasil_tdk_puas_kinerja = 0
    hasil_puas_kinerja = (80 - x_kinerja) / (80 - 60)

if (hasil_puas_kinerja != 0) :
   print('Nilai Memuaskan Kinerja : ',hasil_puas_kinerja)
elif(hasil_tdk_puas_kinerja == 0) : 
    print('Nilai Tidak Memuaskan Kinerja : ',hasil_tdk_puas_kinerja)



# Kedisiplinan
if (x_kedisiplinan <= 60) :
   hasil_tdk_puas_disiplin = (x_kinerja - 60) / (80 - 60)
   hasil_puas_disiplin = 0
elif (x_kedisiplinan > 60 and x_kedisiplinan < 80) :
    hasil_tdk_puas_disiplin = (60 - x_kedisiplinan) / (80 - 60)
    hasil_puas_disiplin = (x_kedisiplinan - 80) / (80 - 60)
elif (x_kedisiplinan >= 80) : 
    hasil_tdk_puas_disiplin = 0
    hasil_puas_disiplin = (80 - x_kedisiplinan) / (80 - 60)

if (hasil_puas_disiplin != 0) :
   print('Nilai Memuaskan Disiplin : ',hasil_puas_disiplin)
elif(hasil_puas_disiplin == 0) : 
    print('Nilai Tidak Memuaskan Disiplin : ',hasil_tdk_puas_disiplin)
    
    
# Kemampuan
if (x_kemampuan <= 60) :
   hasil_tdk_puas_kemampuan = (x_kemampuan - 60) / (80 - 60)
   hasil_puas_kemampuan = 0
elif (x_kemampuan > 60 and x_kemampuan < 80) :
    hasil_tdk_puas_kemampuan = (60 - x_kemampuan) / (80 - 60)
    hasil_puas_kemampuan = (x_kemampuan - 80) / (80 - 60)
elif (x_kemampuan >= 80) : 
    hasil_tdk_puas_kemampuan = 0
    hasil_puas_kemampuan = (80 - x_kemampuan) / (80 - 60)

if (hasil_puas_kemampuan != 0) :
   print('Nilai Memuaskan : ',hasil_puas_kemampuan)
elif(hasil_puas_kemampuan == 0) : 
    print('Nilai Tidak Memuaskan : ', hasil_tdk_puas_kemampuan)
    

# Proses Inferensi
nilai = []
def tidakDapat(y_kinerja, y_kedisiplinan, y_kemampuan) : 
    if y_kinerja != 0 :
        if y_kedisiplinan != 0 :
            if y_kemampuan != 0 :
                iferensi_tidak_dapat = min(y_kinerja, y_kedisiplinan, y_kemampuan)
                z = 50 - (iferensi_tidak_dapat * 10)
                nilai.append([iferensi_tidak_dapat , z])
    
    
def dipertimbangkan(y_kinerja, y_kedisiplinan, y_kemampuan) :
    if y_kinerja != 0 :
        if y_kedisiplinan != 0 :
            if y_kemampuan != 0 : 
                iferensi_dipertimbangkan = min(y_kinerja, y_kedisiplinan, y_kemampuan)
                x = 40 + (iferensi_dipertimbangkan * 10)
                y = 60 - (iferensi_dipertimbangkan * 10)
                z = (x + y) / 2
                nilai.append([iferensi_dipertimbangkan , z])
                        
def dapat(y_kinerja, y_kedisiplinan, y_kemampuan) :
    if y_kinerja != 0 :
        if y_kedisiplinan != 0 :
            if y_kemampuan != 0 :
                iferensi_dapat = min(y_kinerja, y_kemampuan, y_kedisiplinan)
                z = 60 + (iferensi_dapat * 10) 
                nilai.append([iferensi_dapat, z])
#1,2,3,4,5
# Rule
tidakDapat(hasil_tdk_puas_kinerja, hasil_tdk_puas_disiplin, hasil_tdk_puas_kemampuan)
tidakDapat(hasil_tdk_puas_kinerja, hasil_tdk_puas_disiplin, hasil_puas_kemampuan)
tidakDapat(hasil_tdk_puas_kinerja, hasil_puas_disiplin, hasil_tdk_puas_kemampuan)
dipertimbangkan(hasil_tdk_puas_kinerja, hasil_puas_disiplin, hasil_puas_kemampuan)
dipertimbangkan(hasil_puas_kinerja, hasil_puas_disiplin, hasil_tdk_puas_kemampuan)
dipertimbangkan(hasil_puas_kinerja, hasil_tdk_puas_disiplin, hasil_puas_kemampuan)
dipertimbangkan(hasil_puas_kinerja, hasil_tdk_puas_disiplin, hasil_tdk_puas_kemampuan)
dapat(hasil_puas_kinerja, hasil_puas_disiplin, hasil_puas_kemampuan)

new_bagi = 0
new_kali = 0
kali = 0
bagi = 0
for j in range(0, len(nilai)) :
    kali = nilai[j][0] * nilai[j][1]
    bagi = nilai[j][0]
    new_bagi = new_bagi + bagi
    new_kali = new_kali + kali
    
print('Kali ', kali)
print('Bagi ',bagi)
print(new_kali)
print("-"*7)
print(new_bagi)
z = new_kali / new_bagi
print('Z = ' ,z)


# Output
hasil = int(z)
print(' ')
print('| Hasilnya adalah : ')
if (hasil <= 40) :
    print('Tidak dapat Reward')
elif (hasil > 40 and hasil < 60) :
    print('Dipertimbangkan, dapat Reward Rp.50.000')
elif (hasil >= 60) :
    print("Berhak dapat Reward Rp.100.000")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    