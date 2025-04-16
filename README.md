# Machine_Learning_untuk_Predict_NBA_Players_Shot_Made
Membuat model machine learning untuk memprediksi kemungkinan seorang pemain NBA mencetak skor berdasarkan percobaan tembakannya.

## Repository Outline
```
1. README.md - Penjelasan gambaran umum project
2. notebook.ipynb - Notebook yang berisi pengolahan data dengan python dari data loading sampai pembuatan machine learning, dengan model terbaik yang dihasilkan dari cross validation
3. notebook_inf.ipynb - Notebook yang berisi Data Inference yang saya lakukan dengan model yang sudah dibuat
4. folder deployment - Folder yang berisi file yang diperlukan untuk melakukan model deploy
5. basket_court.jpg - file gambar yang saya gunakan didalam notebook.ipynb
6. NBA_Shots _2024.csv - file csv yang berisi dataset yang saya gunakan untuk membuat machine learning
7. url.txt - File yang berisi link model yang sudah saya deploy dengan menggunakan hugging face 
```

## Problem Background
Saya diberikan tugas untuk membuat machine learning yang dapat memprediksi hasil shot yang dilakukan pemain NBA. Diharapkan project ini dapat membantu pemain dalam menemukan posisi dan jenis shot terbaik mereka

## Project Output
Output dari project ini adalah machine learning yang dapat memprediksi hasil shot yang dilakukan pemain NBA dapat menghasilkan point atau tidak

## Data
Data yang digunakan saya ambil dari kaggle degan nama data set NBA_Shot_2024 dengan jumlah kolom 26 dan jumlah baris +/- 200.000, tetapi dalam project ini saya hanya menggunakan 20.000 data dengan game date terbaru 

## Method
Dalam pembuatan machine learning ini saya memutukan menggunakan metode Decision Tree, karena setelah saya melakukan perbandingan dengan metode lain seperti random forest, decision tree dan XG boost dengan cross validation yang menghasilkan bahwa Decision Tree adalah metode terbaik untuk dataset ini

## Stacks
```
Dalam pembuatan machine learning ini saya menggunakan beberapa tools seperti:
1. Bahasa Pemrograman: python
2. Libraries:
    a. pandas
    b. numpy
    c. matplotlib
    d. seaborn
    e. sklearn
    f. feature_engine
    g. xgboost
    h. scipy
```

## Reference
`Saya sudah membuat model deploy, untuk mengakses modelnya anda bisa membuka file url.txt`