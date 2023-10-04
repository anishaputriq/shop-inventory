Anisha Putri Qonitah - 2206083256
PBP D
link adaptable -- tidak bisa deploy :/

<details>
<summary> Tugas 5 </summary>

## Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
### Universal Selector (*):
Manfaat: Selector ini memilih semua elemen dalam halaman.
Kapan Menggunakan: Anda harus sangat hati-hati saat menggunakan universal selector, karena dapat memengaruhi semua elemen di halaman. Sebaiknya hanya digunakan dalam kasus tertentu di mana Anda perlu mengatur beberapa properti CSS secara global.

### Type Selector (Elemen):
Manfaat: Selector ini memilih semua elemen dengan tipe yang cocok (misalnya, p untuk semua elemen paragraf).
Kapan Menggunakan: Cocok digunakan ketika Anda ingin mengatur gaya secara umum untuk tipe elemen tertentu di seluruh situs web.

### ID Selector (#id):
Manfaat: Selector ini memilih elemen berdasarkan ID yang unik.
Kapan Menggunakan: Berguna ketika Anda ingin mengatur gaya untuk elemen yang memiliki ID unik. Sebaiknya hanya digunakan satu kali per halaman karena ID harus unik.

### Class Selector (.class):
Manfaat: Selector ini memilih elemen berdasarkan kelas yang diberikan.
Kapan Menggunakan: Berguna ketika Anda ingin mengatur gaya untuk beberapa elemen yang memiliki kelas yang sama. Anda dapat menggunakannya berkali-kali pada halaman yang berbeda.

### Descendant Selector (Space):
Manfaat: Selector ini memilih elemen yang merupakan keturunan dari elemen lain, di mana elemen keturunan berada dalam elemen yang lebih tinggi dalam struktur dokumen.
Kapan Menggunakan: Berguna ketika Anda ingin mengatur gaya untuk elemen-elemen dalam konteks tertentu, misalnya, semua elemen p dalam elemen div.

### Child Selector (>):
Manfaat: Selector ini memilih elemen yang merupakan anak langsung dari elemen lain.
Kapan Menggunakan: Cocok ketika Anda ingin mengatur gaya untuk elemen yang langsung menjadi anak dari elemen lain, tanpa memperhatikan elemen-elemen lebih dalam dalam struktur.

### Adjacent Sibling Selector (+):
Manfaat: Selector ini memilih elemen yang merupakan saudara sejajar (sibling) dari elemen lain, yang memiliki elemen yang sama dengan elemen lain tersebut.
Kapan Menggunakan: Berguna ketika Anda ingin mengatur gaya untuk elemen yang berdekatan secara langsung dengan elemen lain yang memiliki elemen yang sama.

### General Sibling Selector (~):
Manfaat: Selector ini memilih elemen yang merupakan saudara sejajar (sibling) dari elemen lain yang memiliki elemen yang sama, tanpa memperhatikan posisi relatifnya.
Kapan Menggunakan: Sama seperti adjacent sibling selector, tetapi lebih fleksibel karena tidak harus berdekatan secara langsung.

## Jelaskan HTML5 Tag yang kamu ketahui.
HTML5 (Hypertext Markup Language versi 5) mempunyai banyak tag yang memungkinkan pengembang web untuk merinci struktur halaman web dengan lebih baik dan mengintegrasikan elemen-elemen modern ke dalam desain. Berikut 5 contoh tag:
<header>: Digunakan untuk mendefinisikan header atau bagian atas dari halaman web. Biasanya berisi elemen-elemen seperti judul, logo, dan navigasi.

<nav>: Mengelompokkan elemen-elemen navigasi, seperti menu, dalam satu blok. Ini membantu dalam membuat menu situs web.

<section>: Menggambarkan bagian dari halaman web yang memiliki tema atau konten yang terkait. Berguna untuk memecah konten menjadi bagian-bagian logis.

<article>: Digunakan untuk menandai sebuah artikel atau entitas yang mandiri dalam halaman web. Misalnya, sebuah berita atau posting blog yang dapat berdiri sendiri.

<aside>: Mengidentifikasi konten yang terkait dengan konten di sekitarnya dan biasanya ditempatkan di samping konten utama. Ini sering digunakan untuk iklan atau sidebar.

## Jelaskan perbedaan antara margin dan padding.
### Margin:
Margin adalah ruang di luar elemen, di antara elemen tersebut dan elemen-elemen sekitarnya.
Margin dapat digunakan untuk mengontrol jarak antara elemen dan elemen-elemen lain di sekitarnya atau batasan area elemen terhadap elemen-elemen lain.
Margin tidak memiliki latar belakang atau warna latar belakang dan tidak memengaruhi tampilan elemen itu sendiri.
Jika ada dua elemen dengan margin yang saling bersentuhan, marginnya akan digabungkan sehingga terbentuk margin tunggal di antara keduanya.

### Padding:
Padding adalah ruang di dalam elemen, di antara konten elemen dan tepi elemen itu sendiri.
Padding digunakan untuk mengontrol jarak antara konten elemen dan batasan elemen tersebut.
Padding memiliki latar belakang dan warna latar belakang yang sama dengan elemen itu sendiri, sehingga mempengaruhi tampilan elemen tersebut.
Padding tidak memengaruhi tata letak elemen-elemen sekitarnya, hanya memengaruhi konten di dalam elemen itu sendiri.

Perbedaan kunci antara margin dan padding adalah bahwa margin memengaruhi tata letak elemen di antara elemen-elemen sekitarnya, sedangkan padding memengaruhi tampilan elemen itu sendiri, khususnya pada bagian dalam elemen tersebut.

## Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

### Bootstrap:
Memiliki komponen siap pakai.
Menggunakan banyak class CSS bawaan.
Menyediakan tema bawaan.
Cocok untuk pengembangan cepat atau jika tidak memiliki pengalaman dalam menulis CSS.

### Tailwind CSS:
Menggunakan pendekatan "utility-first."
Memungkinkan customisasi yang tinggi.
Tidak memiliki tema bawaan.
Cocok jika ingin kontrol tinggi terhadap desain atau ingin mengurangi ukuran file CSS.

Bootstrap cocok untuk proyek cepat dengan komponen siap pakai, sedangkan Tailwind cocok untuk proyek yang memerlukan desain yang sangat kustom atau jika memiliki pemahaman yang kuat tentang CSS.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### Kustomisasi desain pada templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut
### Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.
    Di base.html tambahkan meta name dan Bootstrap CSS dan juga JS.
    Tambahkan navigation bar menggunakan Bootstrap pada halaman main.html
    Tambahkan tombol edit di main.html
    Diatas main.html, login.html, edit_product.html, register.html masukan html tag style 
    Isi style dengan warna atau backgroud yang diinginkan

### Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.
    Dalam style ganti backgroud image menjadi gambar yang diinginkan
    Ganti warna tabel dan font
    Tambahkan navigation bar (Bootstrap)
    Pindahkan tombol logout dan add product ke dalam navigation bar

### Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
    menulis jawaban di read.me dan rapihkan 

### Memberikan warna yang berbeda (teks atau background) pada baris terakhir dari item pada inventori anda menggunakan CSS.
    dalam style tambahkan .custom-row.last-row td dan pilih warna yang sesuai dengan keinginan kita
    dalam for loop product <tr class="custom-row{% if forloop.last %} last-row{% endif %}"> agar warna yang diubah adalah baris terakhir
    

### Melakukan add-commit-push ke GitHub.
</details>

<details>
<summary> Tugas 4 </summary>

## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
    Django UserCreationForm adalah salah satu bentuk dari Django's built-in forms yang digunakan untuk membuat formulir pendaftaran pengguna. Form ini memudahkan pengembang web untuk membuat formulir pendaftaran pengguna dengan cepat dan mudah. UserCreationForm memerlukan input seperti username, password, dan konfirmasi password. Kelebihannya termasuk kemudahan penggunaan dan integrasi yang baik dengan sistem otentikasi Django, serta validasi bawaan yang membantu mencegah kesalahan saat pendaftaran pengguna. Kekurangannya adalah kemungkinan kurang fleksibel dalam hal desain, sehingga jika Anda memerlukan tampilan atau fitur pendaftaran yang sangat kustom, Anda mungkin perlu menyesuaikan lebih lanjut.

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
    Autentikasi adalah proses untuk mengidentifikasi pengguna, yaitu memverifikasi apakah seseorang adalah pengguna yang sah dan memberikan akses ke akun mereka. Django memiliki sistem otentikasi yang kuat yang memungkinkan pengguna untuk masuk ke akun mereka dengan menggunakan username dan password atau metode autentikasi lainnya seperti OAuth.

    Otorisasi adalah proses yang mengatur hak akses pengguna yang telah diautentikasi. Ini menentukan apa yang diizinkan atau tidak diizinkan oleh pengguna dalam aplikasi. Django memiliki sistem otorisasi yang memungkinkan pengembang untuk menentukan hak akses berdasarkan peran (roles) pengguna atau izin khusus.

    Keduanya penting dalam konteks Django karena autentikasi memungkinkan Anda untuk mengidentifikasi pengguna yang menggunakan aplikasi Anda, sementara otorisasi memastikan bahwa pengguna hanya dapat mengakses bagian dari aplikasi yang sesuai dengan peran dan izin mereka. Kombinasi keduanya adalah yang membuat aplikasi aman dan mengontrol akses.

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
    Cookies adalah potongan kecil data yang disimpan di sisi klien (browser pengguna) dan dikirim kembali ke server saat permintaan berikutnya. Dalam konteks aplikasi web, cookies digunakan untuk mengelola data sesi pengguna, menyimpan preferensi, atau melacak informasi lainnya yang dibutuhkan dalam beberapa permintaan HTTP berurutan.
    Django menggunakan cookies untuk mengelola sesi pengguna dengan cara yang aman. Ini sering dilakukan dengan menggunakan Django's session framework. Framework ini memungkinkan Anda untuk menyimpan data sesi pengguna di server, sementara cookie yang unik disematkan di sisi klien untuk mengidentifikasi sesi tersebut. Ini membantu menjaga data sesi yang aman, karena data sesi tidak disimpan di sisi klien.

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
    Secara default, penggunaan cookies dalam pengembangan web relatif aman, terutama jika Anda mengikuti praktik terbaik untuk menghindari kerentanan keamanan. Namun, ada beberapa risiko potensial yang perlu diwaspadai:
    Session hijacking: Meskipun Django session framework aman, jika cookies diambil oleh pihak yang tidak sah, mereka dapat mengakses sesi pengguna.
    Cross-Site Scripting (XSS): Jika aplikasi Anda rentan terhadap serangan XSS, penyerang dapat mencuri cookies pengguna.
    Data sensitif: Jika Anda menyimpan data sensitif dalam cookies, risiko keamanan meningkat.
    Untuk mengurangi risiko ini, pastikan untuk mengimplementasikan praktik keamanan seperti mengaktifkan HTTPS, menjalankan validasi di server, dan menghindari penyimpanan data sensitif di cookies. Django sendiri memiliki beberapa perlindungan bawaan untuk mengatasi beberapa risiko ini, tetapi perlu dilakukan penyesuaian tambahan sesuai dengan kebutuhan proyek Anda.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
        jalankan virtual environment
        di view.py buat fungsi register, login, logout 
        import fungsi dan tambahkan path url ke urlpatterns di urls.py
        tambahkan kode login required di atas fungsi show_main

### Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
        import kode untuk fungsi
        runserver, buka web browser localhost
        registrasi akun, lalu buat 3 item baru
        logout dan membuat akun baru dan tambahkan 3 item baru

### Menghubungkan model Item dengan User.
        import model 
        di models.py tambahkan user di item
        di views.py ubah kode create_product dengan menambah request user
        tambahkan request name di context show_main
        migrasi model
        runserver untuk melihat hasilnya

### Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
        mengubah fungsi login dan logout dengan menambahkan informasi cookie last_login 
        menambahkan last_login ke dalam context show_main
        menambahkan kata kata last login ke dalam main.html

### Mengimplementasi Bonus
        membuat fungsi add, decrement dan remove product dalam view.py
        import fungsi, tambahkan path ke urlpatterns
        tambahkan button di main.html

### Melakukan add-commit-push ke GitHub.

</details>

<details>
<summary> Tugas 3 </summary>

## Apa perbedaan antara form POST dan form GET dalam Django?
    Form POST: Ketika mengirimkan formulir dengan metode POST dalam Django, data yang dikirimkan tidak ditampilkan di URL. Data tersebut dikirim sebagai bagian dari tubuh permintaan HTTP, yang tidak terlihat oleh pengguna. Form POST biasanya digunakan untuk mengirim data yang sensitif atau besar, seperti kata sandi atau file.

    Form GET: Dalam form GET, data yang dikirim ditambahkan ke URL sebagai parameter query string. Ini membuat data tersebut dapat dilihat oleh pengguna dan tersimpan dalam riwayat web browser. Form GET biasanya digunakan untuk permintaan yang bersifat idempoten (tidak mengubah data di server) dan ketika ingin data tersebut dapat dibagikan atau disimpan dalam bookmark.

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
    XML (eXtensible Markup Language): XML adalah bahasa markup yang digunakan untuk mengatur dan mengirimkan data terstruktur. Ini sering digunakan dalam pertukaran data antara sistem yang berbeda dan mendukung validasi dengan skema. XML berfokus pada struktur hierarki dan umumnya lebih berat dalam hal sintaksis.

    JSON (JavaScript Object Notation): JSON adalah format pertukaran data yang ringkas dan mudah dibaca oleh mesin dan manusia. Ini berfokus pada objek dan array, membuatnya ideal untuk pertukaran data dalam bahasa pemrograman. JSON sering digunakan dalam aplikasi web modern karena ringkas dan efisien.

    HTML (Hypertext Markup Language): HTML adalah bahasa markup yang digunakan untuk membuat halaman web. Ini berfokus pada presentasi dan struktur tampilan. Meskipun tidak dirancang untuk pertukaran data, HTML sering digunakan untuk menampilkan data dalam tampilan web.

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    JSON ringkas dan mudah dibaca, membuatnya efisien dalam pengiriman data melalui jaringan.
    Dukungan yang luas dalam berbagai bahasa pemrograman membuatnya mudah diimplementasikan dalam berbagai teknologi web.
    JSON mendukung struktur data berbasis objek dan array, yang sesuai dengan cara modern aplikasi web menyusun dan mengelola data.
    JSON mendukung tipe data umum seperti string, angka, boolean, objek, dan array, sehingga cocok untuk berbagai jenis data.
    JSON mendukung data terstruktur dan fleksibel tanpa memerlukan skema yang kaku, memudahkan pengembangan dan evolusi aplikasi.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### Membuat input form untuk menambahkan objek model pada app sebelumnya.
        membuat forms.py untuk menerima data item baru
        import Itemform ke views.py dan buat fungsi baru (create_product) 
### Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
        mengimport httpresponse dan serializers kedalam views.py
        membuat fungsi dengan parameter request yang menyimpan hasil query dari seluruh data yang ada pada Item
        buat semua fungsi untuk HTML, XML, JSON, XML by ID, dan JSON by ID.
### Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
        import fungsi tadi ke urls.py
        tambahkan path url ke urlpatterns
        cek project dengan runserver dan buka localhost 
### Melakukan add-commit-push ke GitHub.
### Menambahkan pesan "Kamu menyimpan X item pada aplikasi ini" (dengan X adalah jumlah data item yang tersimpan pada aplikasi) dan menampilkannya di atas tabel data
        dalam views.py show_main buat variabel baru dengan nama item yang menyimpan nilai jumlah semua item dengan cara item.object.count
        dalam main.html tambahkan {{item}} dan kata-katanya

## Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
### HTML
 ![gambar postman HTML](https://github.com/anishaputriq/shop-inventory/blob/main/gambar%20postman/HTML.png)
### XML
 ![gambar postman XML](https://github.com/anishaputriq/shop-inventory/blob/main/gambar%20postman/XML.png)
### JSON
 ![gambar postman JSON](https://github.com/anishaputriq/shop-inventory/blob/main/gambar%20postman/JSON.png)
### XML BY ID
 ![gambar postman XML BY ID](https://github.com/anishaputriq/shop-inventory/blob/main/gambar%20postman/XML%20ID.png)
### JSON BY ID
 ![gambar postman JSON BY ID](https://github.com/anishaputriq/shop-inventory/blob/main/gambar%20postman/JSON%20ID.png)


</details>

<details>
<summary> Tugas 2 </summary>

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### Membuat sebuah proyek Django baru.
    buat direktori baru dan hubungkan dengan repositori
    buka cmd dan jalankan django-admin startproject shopping-inventory .

### Membuat aplikasi dengan nama main pada proyek tersebut.
    aktifkan virtual environment
    di cmd jalankan python manage.py startapp main

### Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
    buka berkas urls.py di direktori main
    Tambahkan path untuk aplikasi 'main' dalam urlpatterns

### Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
    name sebagai nama item dengan tipe CharField.
    amount sebagai jumlah item dengan tipe IntegerField.
    description sebagai deskripsi item dengan tipe TextField.
    dalam models.py bikin class dengan nama Item dan bikin atribut diatas dengan tipe seperti ketentuan

### Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    buka view.py di direktori main
    tambahkan fungsi dictionary yang mengembalikan template HTML yang menampilkan nama 

### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
    buka urls.py di direktori main
    tambahkan path untuk fungsi yang telah dibuat di views.py

### Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    buka site adaptable, connect dengan git hub dan pilih repo yang dibuat dan deploy dengan python template!

### Membuat sebuah README.md
        di dalam direktori buat file README.md dan tulis jangan lupa di commit push

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
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

## Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Kita dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapu sangat disarankan untuk menggunakan venv untuk mengelola dependensi proyek secara efisien, meminimalkan potensi konflik, mengurangi risiko menyebabkan masalah di lingkungan Python global, pemeliharaan virtual environment lebih mudah, dan membuat proyek lebih mudah dikelola dan dipelihara.

## Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
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

</details>