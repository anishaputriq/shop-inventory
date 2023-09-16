Anisha Putri Qonitah - 2206083256
PBP D
link adaptable -- tidak bisa deploy :/

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    = Membuat sebuah proyek Django baru.
        buat direktori baru dan hubungkan dengan repositori
        buka cmd dan jalankan django-admin startproject shopping-inventory .

    = Membuat aplikasi dengan nama main pada proyek tersebut.
        aktifkan virtual environment
        di cmd jalankan python manage.py startapp main

    = Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
        buka berkas urls.py di direktori main
        Tambahkan path untuk aplikasi 'main' dalam urlpatterns

    = Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
    name sebagai nama item dengan tipe CharField.
    amount sebagai jumlah item dengan tipe IntegerField.
    description sebagai deskripsi item dengan tipe TextField.
        dalam models.py bikin class dengan nama Item dan bikin atribut diatas dengan tipe seperti ketentuan

    = Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
        buka view.py di direktori main
        tambahkan fungsi dictionary yang mengembalikan template HTML yang menampilkan nama 

    = Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
        buka urls.py di direktori main
        tambahkan path untuk fungsi yang telah dibuat di views.py

    = Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
        buka site adaptable, connect dengan git hub dan pilih repo yang dibuat dan deploy dengan python template!
    = Membuat sebuah README.md
        di dalam direktori buat file README.md dan tulis jangan lupa di commit push

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    ![gambar bagan](https://github.com/anishaputriq/shop-inventory/blob/e3529d0b2f349cdaf59896699462609fb1181479/bagan%20.png)
    urls.py mengatur bagaimana URL akan di-mapping ke view yang spesifik.
    views.py berisi view yang mengatur logika aplikasi dan berkomunikasi dengan model jika perlu. View ini mengembalikan respons berdasarkan permintaan yang diterimanya.
    models.py mendefinisikan struktur basis data dan kelas-kelas model yang dapat digunakan oleh aplikasi Anda. View dapat menggunakan model ini untuk berinteraksi dengan basis data.
    Berkas HTML digunakan untuk merender tampilan yang akan ditampilkan kepada pengguna, dan views dapat mengirimkan data yang diperlukan ke berkas HTML ini untuk disajikan kepada pengguna.

    alur umumnya adalah sebagai berikut:
    Pengguna membuat permintaan melalui URL yang didefinisikan di urls.py.
    urls.py akan mengarahkan permintaan tersebut ke view yang sesuai di views.py.
    View di views.py akan mengambil data dari model (jika diperlukan) dan menghasilkan respons.
    Respons yang dihasilkan akan ditampilkan kepada pengguna melalui berkas HTML yang sesuai.

Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Kita dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapu sangat disarankan untuk menggunakan venv untuk mengelola dependensi proyek secara efisien, meminimalkan potensi konflik, mengurangi risiko menyebabkan masalah di lingkungan Python global, pemeliharaan virtual environment lebih mudah, dan membuat proyek lebih mudah dikelola dan dipelihara.

Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
    MVC, MVT, dan MVVM adalah pola arsitektur perangkat lunak yang digunakan dalam pengembangan aplikasi berbasis web dan aplikasi perangkat lunak pada umumnya.

    Pengertian:
    MVC (Model-View-Controller): Ini adalah pola arsitektur yang memisahkan aplikasi menjadi tiga komponen utama: Model (untuk data dan logika bisnis), View (untuk tampilan), dan Controller (untuk mengontrol aliran aplikasi).
    MVT (Model-View-Template): Digunakan terutama dalam kerangka kerja web Django, MVT menggantikan Controller dalam MVC dengan komponen View yang mengelola tampilan dan Template yang mengontrol tampilan HTML.
    MVVM (Model-View-ViewModel): MVVM adalah pola arsitektur yang umumnya digunakan dalam pengembangan aplikasi berbasis klien modern. Ini memiliki Model (untuk data dan logika bisnis), View (untuk tampilan), dan ViewModel (untuk mengelola tampilan dan presentasi data, bertindak sebagai perantara antara Model dan View).

    Perbedaan: 
    MVC menggunakan Controller sebagai perantara antara Model dan View, sementara MVT menggunakan View langsung untuk berkomunikasi dengan Model. Dalam MVT, Controller digantikan oleh View dan Template.
    MVVM memiliki komponen ViewModel yang khusus untuk mengelola tampilan dan presentasi data. Ini memisahkan tugas Controller dan View dalam pengembangan.
    MVC dan MVT lebih umum digunakan dalam pengembangan aplikasi web berbasis server, sedangkan MVVM sering digunakan dalam pengembangan aplikasi berbasis klien (seperti aplikasi desktop atau aplikasi seluler).
    MVT khusus digunakan dalam kerangka kerja web Django.

...............................................................................................................

Tugas 3
Apa perbedaan antara form POST dan form GET dalam Django?

Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    Membuat input form untuk menambahkan objek model pada app sebelumnya.
    Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

    Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

    Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

    Melakukan add-commit-push ke GitHub.