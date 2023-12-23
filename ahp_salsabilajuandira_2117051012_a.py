# -*- coding: utf-8 -*-
"""AHP_SalsabilaJuandira_2117051012_A.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AiW1ndVPRG960v2V7Khl7yY_zuakRu-g

#AHP (Analytic Hierarchy Process)
Nama: Salsabila Juandira<br>
NPM: 2117051012<br>
Kelas: A

#Study Case
Pemilihan tas wanita dengan 3 kriteria yaitu:<br>
* Harga
* Model
* Kualitas<br>

dan 3 alternatif merk tas yaitu:<br>
* Charles&Keith
* Zara
* H&M

# Library
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import normalize

"""#AHP Function"""

def calculate_priority(features, total_point):
  n = len(features[0])
  ahp_matrix = np.ones([n, n])

  for i in range(0, n): # baris
    for j in range(0, n): # kolom
      if(i < j):
        if(i == 0):
          ahp_matrix[i, j] = float(features[1][j-1])
          ahp_matrix[j, i] = float(1/features[1][j-1])
        else:
          if(ahp_matrix[0, j] < ahp_matrix[0, i]):
            ahp_matrix[i, j] = float(1/((ahp_matrix[0, i] - ahp_matrix[0, j]) + 1))
          else:
            ahp_matrix[i, j] = float((ahp_matrix[0, j] - ahp_matrix[0, i]) + 1)
          ahp_matrix[j, i] = float(1/ahp_matrix[i,j])

  normalized_matrix = normalize(ahp_matrix, axis=0, norm="l1")
  weight = normalized_matrix.mean(1)

  points = total_point*weight

  return dict(zip(features[0], points))

"""#Feature Priority"""

features = ['Model','Harga','Kualitas']
feature_scores = calculate_priority([features, [4,3]], 1)
feature_scores

"""#Brand Comparisson"""

#Dilihat dari segi model
skor_model = calculate_priority([['Zara','Charles&Keith','H&M'], [4, 3]],1)
skor_model

#Dilihat dari soal harga
skor_harga = calculate_priority([['Charles&Keith','Zara','H&M'], [3, 5]],1)
skor_harga

#Dilihat dari segi Kualitas
skor_kualitas = calculate_priority([['Charles&Keith','H&M','Zara',], [2, 3]],1)
skor_kualitas

"""#AHP Table"""

df = pd.DataFrame([skor_model, skor_harga, skor_kualitas])
df.index = feature_scores.keys()
df

total = df.sum(axis=0)
total.name = 'Total Score'
df = pd.concat([df, total.to_frame().T])
df

"""#Kesimpulan
Berdasarkan perhitungan menggunakan metode AHP diatas didapatkan bahwa brand Charles&Keith memiliki skor yang tinggi sehingga direkomendasikan menjadi brand tas wanita yang layak untuk dibeli karena harga yang memiliki skor harga dan kualitas yang tinggi.
"""