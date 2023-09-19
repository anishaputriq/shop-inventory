Anisha Putri Qonitah - 2206083256
PBP D
link adaptable -- tidak bisa deploy :/

Tugas 3
Apa perbedaan antara form POST dan form GET dalam Django?
    Form POST: Ketika mengirimkan formulir dengan metode POST dalam Django, data yang dikirimkan tidak ditampilkan di URL. Data tersebut dikirim sebagai bagian dari tubuh permintaan HTTP, yang tidak terlihat oleh pengguna. Form POST biasanya digunakan untuk mengirim data yang sensitif atau besar, seperti kata sandi atau file.

    Form GET: Dalam form GET, data yang dikirim ditambahkan ke URL sebagai parameter query string. Ini membuat data tersebut dapat dilihat oleh pengguna dan tersimpan dalam riwayat web browser. Form GET biasanya digunakan untuk permintaan yang bersifat idempoten (tidak mengubah data di server) dan ketika ingin data tersebut dapat dibagikan atau disimpan dalam bookmark.

Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
    XML (eXtensible Markup Language): XML adalah bahasa markup yang digunakan untuk mengatur dan mengirimkan data terstruktur. Ini sering digunakan dalam pertukaran data antara sistem yang berbeda dan mendukung validasi dengan skema. XML berfokus pada struktur hierarki dan umumnya lebih berat dalam hal sintaksis.

    JSON (JavaScript Object Notation): JSON adalah format pertukaran data yang ringkas dan mudah dibaca oleh mesin dan manusia. Ini berfokus pada objek dan array, membuatnya ideal untuk pertukaran data dalam bahasa pemrograman. JSON sering digunakan dalam aplikasi web modern karena ringkas dan efisien.

    HTML (Hypertext Markup Language): HTML adalah bahasa markup yang digunakan untuk membuat halaman web. Ini berfokus pada presentasi dan struktur tampilan. Meskipun tidak dirancang untuk pertukaran data, HTML sering digunakan untuk menampilkan data dalam tampilan web.

Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    JSON ringkas dan mudah dibaca, membuatnya efisien dalam pengiriman data melalui jaringan.
    Dukungan yang luas dalam berbagai bahasa pemrograman membuatnya mudah diimplementasikan dalam berbagai teknologi web.
    JSON mendukung struktur data berbasis objek dan array, yang sesuai dengan cara modern aplikasi web menyusun dan mengelola data.
    JSON mendukung tipe data umum seperti string, angka, boolean, objek, dan array, sehingga cocok untuk berbagai jenis data.
    JSON mendukung data terstruktur dan fleksibel tanpa memerlukan skema yang kaku, memudahkan pengembangan dan evolusi aplikasi.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    Membuat input form untuk menambahkan objek model pada app sebelumnya.
        membuat forms.py untuk menerima data item baru
        import Itemform ke views.py dan buat fungsi baru (create_product) 
    Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
        mengimport httpresponse dan serializers kedalam views.py
        membuat fungsi dengan parameter request yang menyimpan hasil query dari seluruh data yang ada pada Item
        buat semua fungsi untuk HTML, XML, JSON, XML by ID, dan JSON by ID.
    Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
        import fungsi tadi ke urls.py
        tambahkan path url ke urlpatterns
        cek project dengan runserver dan buka localhost 
    Melakukan add-commit-push ke GitHub.
    Menambahkan pesan "Kamu menyimpan X item pada aplikasi ini" (dengan X adalah jumlah data item yang tersimpan pada aplikasi) dan menampilkannya di atas tabel data
        dalam views.py show_main buat variabel baru dengan nama item yang menyimpan nilai jumlah semua item dengan cara item.object.count
        dalam main.html tambahkan {{item}} dan kata-katanya

Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
HTML
 ![gambar postman HTML](https://github.com/anishaputriq/shop-inventory/blob/main/gambar%20postman/HTML.png)
 XML
 ![gambar postman XML](https://github.com/anishaputriq/shop-inventory/blob/main/gambar%20postman/XML.png)
 JSON
 ![gambar postman JSON](https://github.com/anishaputriq/shop-inventory/blob/main/gambar%20postman/JSON.png)
 XML BY ID
 ![gambar postman XML BY ID](https://github.com/anishaputriq/shop-inventory/blob/main/gambar%20postman/XML%20ID.png)
 JSON BY ID
 ![gambar postman JSON BY ID](https://github.com/anishaputriq/shop-inventory/blob/main/gambar%20postman/JSON%20ID.png)

...............................................................................................................

Tugas 2
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