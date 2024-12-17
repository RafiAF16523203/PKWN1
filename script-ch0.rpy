# Ren'Py Script for "Petualangan Sang Jaka Pradnya Nuraga"
# Define characters and backgrounds
define a = Character("Anthony", color="#aabbcc")
define a_neutral = Character("Anthony", color="#aabbcc")
define a_happy = Character("Anthony", color="#aabbcc")
define a_scared = Character("Anthony", color="#aabbcc")
define a_worried = Character("Anthony", color="#aabbcc")
define a_happy2 = Character("Anthony", color="#aabbcc")
define a_neutral2 = Character("Anthony", color="#aabbcc")
define a_shocked2 = Character("Anthony", color="#aabbcc")
define a_worried2 = Character("Anthony", color="#aabbcc")
define k = Character("Ki Joyo Renggana", color="#ddaabb")
define raja = Character("Sri Maharaja K", color="#ffcc88")
define raja_marah = Character("Sri Maharaja K", color="#ffcc88")
define raja_netral = Character("Sri Maharaja K", color="#ffcc88")
define raja_panik = Character("Sri Maharaja K", color="#ffcc88")
define raja_senyum = Character("Sri Maharaja K", color="#ffcc88")
define raja_serius = Character("Sri Maharaja K", color="#ffcc88")
define raja_pointing = Character("Sri Maharaja K", color="#ffcc88")
define p = Character("Pedagang", color="#77bb77")
define y = Character("Prabu Wijayapranata", color="#ff5577")
define s = Character('Siswi', color="#00FFFF")
define ajudan = Character("Ajudan", color="#FF0000")
define ajudan_run = Character("Ajudan", color="#FF0000")
define ajudan_salute = Character("Ajudan", color="#FF0000")
define mysterious_man = Character("Mysterious Man", color="#f700ff")
define citizen = Character("Warga", color="#bbcc77")
define citizen_a_neutral = Character("Warga A", color="#bbcc77")
define citizen_a_smirk = Character("Warga A", color="#bbcc77")
define citizen_b_angry = Character("Warga B", color="#455507")
define citizen_b_neutral = Character("Warga B", color="#455507")
define citizen_c_neutral = Character("Warga C", color="#cdea5d")
define citizen_c_scared = Character("Warga C", color="#cdea5d")
define guard = Character("Penjaga", color="#88aaff")
define satpam = Character("Satpam", color="#88aaff")
define Kakek = Character('Kakek', color="#9e1f0c")
define Pedagang = Character('Pedagang', color="#FFD700")
define g = Character('Bu Mega', color="#8A2BE2")


# Define chara
# Define chara
## image citizen_riot = "images/"
image a  = "images/Anthony_netral (1).png"
image s = "images/Siswi_sma_npc.png" 
image a_happy = "images/Anthony_happy.png"
image a_neutral2 = "images/Anthony2_netral.png"
image a_happy2 = "images/Anthony2_happy.png"
image a_scared = "images/Anthony_scared_shocked.png"
image a_scared2 = "images/Anthony2_shocked.png"
image a_worried = "images/Anthony_worried.png"
image a_worried2 = "images/Anthony2_worried.png"
# image ajudan_salute = "images/"
image ajudan_run = "images/Ajudan1_adegan lari.png"
image ajudan_salute = "images/Ajudan2 berdiri.png"
image citizen_trio_neutral = "images/Bertiga (netral).png"
image citizen_trio_exp = "images/Bertiga (dg reaksi).png"
image citizen_a_neutral = "images/PendudukA_netral.png"
image citizen_a_smirk = "images/PendudukA_snyum licik.png"
image citizen_b_angry = "images/PendudukB_marah.png"
image citizen_b_neutral = "images/PendudukB_netral.png"
image citizen_c_neutral = "images/PendudukC_netral.png"
image citizen_c_scared = "images/PendudukC_takut.png"
image satpam = "images/Satpam_600x800.png"
image raja_angry = "images/Raja_marah.png"
image raja_neutral = "images/Raja_netral.png"
image raja_panic = "images/Raja_panik.png"
image raja_smile = "images/Raja_senyum.png"
image raja_serius = "images/Raja_serius.png"
image raja_pointing = "images/Rajav2_menunjuk_memerintah.png"
image a fall down = "images/A jatuh ke lubang.jpg"
image a woke up = "images/1280x720 A bangun di kelas.png"
image a lusuh = "images/1280x720 A pakai bju lusuh.png"
image ajudan run 2 = "images/Ajudan1 lari dihutan revisi.png"
image teacher = "images/Bu guru.PNG"
image Kakek = "images/IMG_2295.PNG"



# Define backgrounds
define bg_palace = "backgrounds/palace.jpg"
define bg_market = "backgrounds/market.jpg" 
define bg_ruins = "backgrounds/ruins.jpg"
define bg_house = "backgrounds/house.jpg"
define bg_forest = "backgrounds/forest.jpg"

# Define sounds
define s_rumor = "sounds/rumor.ogg"
define s_conflict = "sounds/conflict.ogg"
define s_wind = "sounds/wind.ogg"
define s_market = "sounds/market.ogg"

# Define bg 
image bg classroom = "images/915374_0.jpg"
image bg forest = "images/915367_0.jpg"
image bg palace = "images/915366_0.jpg"
image bg school = "images/CompressJPEG.online_1280x720_image.jpeg.png"
image bg market = "images/915368_0.jpg"
image bg house = "images/915369_0.jpg"
image bg inside building = "images/915371_0.jpg"
image bg lorong = "images/915370_0.jpg"
image bg ruins = "images/915372_0.jpg"

define A = Character('A', color="#aabbcc")
define Kakek = Character('Kakek', color="#FF6347")
define Pedagang = Character('Pedagang', color="#FFD700")
define Raja = Character('Raja', color="#8A2BE2")
define Warga = Character('Warga', color="#228B22")
define Pedagang_smiling = Character('Pedagang', color="#FFD700")




# The game starts here.
# Mulai game
label start:
    scene bg forest with fade
    play music "Frame 1#1.mp3"
    show ajudan run 2 at center
    "Seorang Ajudan Raja berlari terengah-engah melalui hutan, wajahnya panik dan terburu-buru."
    scene bg palace with fade
    "Ajudan Raja tiba di istana dan memberi laporan pada Raja."
    stop music fadeout 1.75
    play music "audio_hero_911_SIPML_J-0501.mp3"
    ajudan "Yang Mulia, gawat, hamba telah mendengar bahwa kerajaan Y sebentar lagi akan menyerang."
    show raja_panic at Position(xalign=0.5,yalign=-0.8)
    "Raja pun terkejut mendengar hal ini, lalu Ia langsung memberi perintah."
    show raja_neutral at Position(xalign=0.5,yalign=-0.8)
    raja'Segera beri peringatan kepada rakyat dan perkuat pertahanan di dermaga!'
    
    "Ajudan Raja bergegas keluar untuk menyebarkan perintah."

    ajudan'Akan hamba laksanakan, Yang Mulia!'
    stop music fadeout 1.75
    # Transition ke bagian sekolah SMA
    scene bg school with fade
    play music "zapsplat_transport_car_motorway_inside_window_open_slight_air_cars_pass_slow.mp3"
    
    "Di SMA, hari pertama dimulai, dengan siswa-siswa yang bergerombol."
    stop music fadeout 1.75
label school_intro:
    play music "audio_hero_HighSchoolGymnasiu+PE375601.mp3"
    "Anthony, seorang siswa SMA yang terkenal sombong, terlihat berjalan sendirian dengan barang-barang branded."
    show a at Position(xalign=0.0, yalign=0.0, yoffset=50)
    a'Tentu saja, semuanya tahu siapa aku!'
    
    show s at Position(xalign=1.0, yalign=0.0, yoffset=-50)
    s'Itu Anthony, anak orang kaya, ya?'
    
    show a at Position(xalign=0.0, yalign=0.0, yoffset=50) #close up
    a'(dalam hati) Apa pedulinya mereka?'
    
    hide s
    "Anthony kemudian masuk ke kelas dan duduk dengan malas."
    play sound "Pintu kelas terbuka.mp3"
    show bg classroom with fade
    a'Tck, buat apa sih sekolah, pagi-pagi udah bikin males'
    
    "Guru masuk ke kelas dan memulai pembelajaran tentang Kerajaan X dan Y."
    show teacher at Position(xalign=0.5,yalign=-0.8)
    g'Hari ini kita akan belajar tentang Kerajaan X dan Y. Dua kerajaan yang bertempur tanpa perang fisik.'
    
    "Anthony mulai merasa bosan dan meminta izin ke toilet."
    show a at Position(xalign=0.0, yalign=0.0, yoffset=50)
    a'Bu, izin ke toilet.'
    
    show teacher at Position(xalign=0.5,yalign=-0.8)
    g'Ayo cepat kembali ya!?'
    

    "Anthony pun pergi meninggalkan kelas dengan senyum licik."
    hide teacher
    scene bg school with fade
    "Anthony berjalan-jalan ke kantin, namun tiba-tiba seorang satpam melihatnya."
    show satpam at Position(xalign=0.0, yalign=0.5, yoffset=50)
    satpam'Hei! Siswa! Mau ke mana?!'

    "Anthony pun berlari mencoba menghindar."
    show a at Position(xalign=0.5,yalign=-0.8)
    play sound "running.mp3"
    a"(dalam hati) Pasti dia tidak akan bisa mengejarku!"
    stop music fadeout 1.75
    # Scene jatuh ke dalam lubang
    play sound "falling.mp3"
    "Tiba-tiba Anthony jatuh ke dalam lubang besar!"
     
    scene a fall down with fade
    a"AAAAAH!"

    hide satpam
    show bg market with fade
    "Anthony terjatuh dan tersadar di suatu tempat yang asing."
    play music "Suara rakyat berkerumun.mp3"
    show a_worried at Position(xalign=0.5,yalign=-0.8)
    a"'Hah? Aku di mana ini?'"
    
    # Transition ke Kerajaan X
    scene bg market with fade
    "Anthony menemukan dirinya berada di tengah kerumunan rakyat di sebuah pasar tradisional."
    "Anthony melihat seorang Ajudan Raja sedang membaca perintah di depan kerumunan."
    show ajudan_salute at Position(xalign=0.0, yalign=-1.0, yoffset=-50)
    ajudan"'Kerajaan Y akan menyerang! Persiapkan dirimu!'"
    hide ajudan_salute
    show a_worried at Position(xalign=0.0, yalign=-1.0, yoffset=-50)
    "Anthony merasa bingung, apakah ia telah terlempar ke masa lalu?"
    a"(dalam hati) 'Kerajaan X? Nama itu terdengar familiar... Apa aku ada di masa lalu?'"
    hide a_worried
    stop music fadeout 1.75
# Define the characters first (e.g., A = Main character, Kakek = Old man, Pedagang = Merchant)
define A = Character('A', color="#aabbcc")
define Kakek = Character('Kakek', color="#FF6347")
define Pedagang = Character('Pedagang', color="#FFD700")
define Raja = Character('Raja', color="#8A2BE2")
define Warga = Character('Warga', color="#228B22")
define Pedagang_smiling = Character('Pedagang', color="#FFD700")

# Start of the game
label waw:

    # Frame 30: A & Kakek's Conversation
    scene bg market with fade
    show Kakek at Position(xalign=1,yalign=-0.8, yoffset=50)
    show a at Position(xalign=0.5,yalign=-0.8, yoffset=50)
    play music "Rakyat Berbicara Samar Samar.mp3"

    "A mulai mencari bantuan dari seorang kakek tua yang berjualan di pasar."
    "'Permisi Kakek, apakah Kakek bisa membantu? Aku tersesat dan tidak tahu jalan pulang.'"
    stop music fadeout 1.75
    play music "bg.mp3"
    Kakek "Kamu pasti bukan dari sini, Le. Kasihan sekali, apakah kamu mau ikut Kakek sampai orang tuamu menjemputmu?"
    
    a "Baik Kakek, terimakasih banyak."
    stop music fadeout 1.75
    # Transition to next scene
    scene bg forest with dissolve    
    play sound "suara jangkrik(sudah malam hari).mp3"
    "Malam pun tiba, dan Anthony mengajak ngobrol kakek"
    stop sound fadeout 1.75
    with fade
    
    # Frame 33: a & Kakek in the house
    scene bg house with fade
    show Kakek at Position(xalign=1,yalign=-0.8, yoffset=50)
    show a at Position(xalign=0.5,yalign=-0.8, yoffset=50)
    play music "bg.mp3"
    
    a "Apakah kakek sudah mendengar berita penyerangan? Bukankah seharusnya seluruh masyarakat panik dan bersiap?"
    
    Kakek "Memang, di luar sana orang-orang berusaha melindungi harta bendanya sampai-sampai mereka lupa dengan apa yang sedang terjadi."
    
    a "Bagaimana jika aku berusaha menyelidiki bagaimana caranya mengalahkan Kerajaan Y, mungkin dengan berbaur dengan rakyat sekitar?"
    
    Kakek "Mulia sekali tindakanmu, Le! Anak muda seperti kamu ini memang memiliki semangat juang tinggi, ambillah bajuku di lemari jika kau mau,   gunakanlah agar kamu tidak terlihat mencolok di sekitar."
    
    # Show a gearing up (wearing traditional clothes)
    scene bg house with fade
    show a_neutral2 at Position(xalign=0.5,yalign=-0.8)
    
    # Game interface: Start options
    "Apakah Teman-teman mau Berpetualang Bersama denganku?"
    menu:
        "Start":
            jump start_adventure
        "Quit":
            return

# Transition to the next part
label start_adventure:
    scene bg market with fade
    play music "lagu menegangkan.mp3"
    
    "Lokasi pertama yang A teliti adalah Pasar Tradisional, sesuai dengan saran Kakek, Kakek berkata bahwa pedagang di Pasar Tradisional adalah penyimpan dan penyampai pesan terbaik di seluruh kerajaan."
    stop music fadeout 1.75
    # First choice of action
    menu:
        "A bertanya kepada Pedagang":
            jump ask_merchants
        "A bertanya pada seorang asing":
            jump follow_stranger

# Scene 1: A asraja merchant
label ask_merchants:
    scene bg market with fade
    show citizen_a_neutral at Position(xalign=1,yalign=-0.8, yoffset=50)
    show a_neutral2 at Position(xalign=0.5,yalign=-0.8, yoffset=50)
    play music "Suara rakyat berkerumun.mp3"
    a "Apa yang sedang terjadi akhir-akhir ini ya pak?"
    
    Pedagang "Banyak sekali Le, kami para pedagang sangat kesulitan mendapatkan pembeli, meskipun harga sudah lebih murah dari biasanya."
    
    a "…. (terdiam)"
    
    Pedagang "Pedagang di ujung sana terlihat lebih laku dan mendapatkan lebih banyak keuntungan, anehnya pelanggan setia kami juga memutuskan untuk berganti langganan."
    
    a "Hmm, Persaingan harganya terlihat tidak sehat."
    
    a "Apakah Bapak dapat menunjukkan jalan menuju tempat para pedagang itu? Aku ingin mengetahui asal mereka."
    
    Pedagang "Ikuti salah satu orang yang memasuki lorong tersebut Le! Lorong itu akan membawamu ke tempat tersebut."
    stop music fadeout 1.75
    jump investigate_building

# Scene 2: Following the stranger
label follow_stranger:
    scene bg inside building with fade
    show a_neutral2 at Position(xalign=0.5,yalign=-0.8)
    
    "Anthony menguntit orang tersebut dan melihat keanehan pada gedung tua dimana banyak orang berlalu lalang menjadi pedagang asing. Orang asing tersebut tidak menyadari ia diuntit, akan tetapi bergerak dengan cepat."
    
    # Show A observing the strange building
    show a_neutral2 at Position(xalign=0.5,yalign=-0.8, yoffset=-50) with fade
    
    a "Darimana produk tersebut berasal? Produk apa yang mereka jual sampai-sampai semua orang membeli dan memilikinya?"
    
    jump investigate_building

# Scene: A investigates the building
label investigate_building:
    scene bg lorong with fade
    show a_neutral2 at Position(xalign=0.5,yalign=-0.8)
    play music "Suara rakyat berkerumun.mp3"
    a "Hm, sepertinya barang-barang ini terlihat asing dan memiliki kualitas yang jauh lebih baik daripada barang di pasar tradisional, seperti bukan dari sini.."
    
    "Untuk mengetahuinya aku akan mencoba membeli salah satu barang ini menggunakan uang saku dari Kakek!"
    stop music fadeout 1.75
    jump buy_item

# Scene: A buys an item from the merchant
label buy_item:
    scene bg lorong with fade
    show citizen_b_neutral at Position(xalign=1,yalign=-0.2, yoffset=50)
    show a_neutral2 at Position(xalign=0.5,yalign=-0.8, yoffset=50)
    play music "Suara rakyat berkerumun.mp3"
    a "Pak, saya beli ini 1 ya."
    
    Pedagang_smiling "Omong-omong, apakah Bapak baru disini? Saya belum pernah melihat gedung ini sebelumnya."
    
    Pedagang "Yah, bisa dibilang begitu, Nak."
    
    a "Wah, sepertinya ada yang tidak beres dengan semua ini.."
    stop music fadeout 1.75
    jump suspicious_activity

# Scene: Pedagang's secret plan revealed
label suspicious_activity:
    scene bg palace with fade
    show raja_neutral at Position(xalign=0.5,yalign=-0.8)
    
    "Raja kerajaan Y memang cerdas, peperangan tidak selalu harus bersifat fisik, tetapi memang penjajahan ekonomi seperti ini jauh lebih efektif!"
    
# Lanjutan dari FRAME XX

label frame_xx:
    scene bg market with fade
    show a_neutral2 at Position(xalign=0.5,yalign=-0.8, yoffset=50)
    play music "Suara rakyat berkerumun.mp3"
    "Anthony berjalan keluar dari gedung, sambil memakan makanan yang baru saja ia beli."
    a "Wah, barang yang dijual memang jauh lebih murah dan lebih enak!"

    narrator "Karena perilaku A yang konsumtif, ia melupakan misi sebenarnya dari penyelidikan dan kembali ke pasar untuk membeli barang-barang lain."

label part_ii:
    scene bg market with fade
    show a_neutral2 at Position(xalign=0.5,yalign=-0.8, yoffset=50)
    show Kakek at Position(xalign=1,yalign=-0.8, yoffset=50)
    play music "Suara rakyat berkerumun.mp3"
    narrator "Anthony menikmati makanan dan baju-baju modern yang ia beli dengan harga murah dari pedagang asing."
    
    Kakek "Barang apa saja yang kamu beli, Le? Jangan terbiasa untuk bersikap konsumtif seperti itu, kita harus berhemat untuk mengantisipasi banyak hal."

    a "Aku bukan konsumtif kok, Lihat saja, orang-orang juga melakukan hal yang sama."

    Kakek "Banyak yang melakukan bukan berarti hal tersebut benar. Jika diamati, sepertinya Kakek belum pernah melihat produk-produk ini. Dimana kamu mendapatkannya, Le?"

    a "Setelah aku menyusuri sebuah jalan, aku menemukan gedung besar baru. Pedagang-pedagang berkumpul di sana menjual produk dengan harga jauh lebih murah daripada pasar tradisional, dan kualitasnya jauh lebih baik!"

    Kakek "Hmm, Kakek setuju, tapi coba cermati kembali apa saja yang sudah kau temukan hari ini."
    stop music fadeout 1.75
    menu:
        "Tidak Mendengarkan Kakek":
            jump ignore_Kakek

        "Mendengarkan Kakek":
            jump listen_to_Kakek

label ignore_Kakek:
    scene bg market with fade
    show a_neutral2 at Position(xalign=0.5,yalign=-0.8)
    play music "Suara rakyat berkerumun.mp3"
    narrator "Anthony tidak mempedulikan nasihat Kakek dan terus membeli barang, bahkan menjual barang-barangnya untuk mendapatkan lebih banyak barang. Ia semakin tidak peduli dengan keadaan sekitar."

    a "Aku tidak bisa berhenti! Ada begitu banyak barang bagus yang harus dibeli!"


    narrator "Setiap interaksi memperlihatkan koin yang semakin berkurang, menunjukkan konsekuensi dari pilihan A."
    stop music fadeout 1.75
    jump part_ii

label listen_to_Kakek:
    scene bg market with fade
    show a_neutral2 at Position(xalign=0.5,yalign=-0.8)

    play music "Suara rakyat berkerumun.mp3"
    narrator "Anthony mendengarkan pesan Kakek dan mulai mencari perbedaan antara pedagang di gedung baru dan pasar tradisional."

    "Bantu Anthony untuk menemukan perbedaan antara para pedagang!"

    narrator "Anthony menyadari bahwa para pedagang bukan berasal dari Kerajaan X, berdasarkan penampilan yang mencurigakan, bahasa asing yang mereka gunakan, dan sikap gugup mereka."

    a "Waduh, dengan semua perbedaan tersebut, pedagang-pedagang ini tidak mungkin berasal dari Kerajaan X! Aku harus mengambil tindakan segera!"
    stop music fadeout 1.75
    menu:
        "Memberi tahu Raja":
            jump inform_raja

        "Menyebarkan Kabar ke Warga":
            jump inform_citizen

label inform_raja:
    scene bg palace with fade
    show raja_neutral at Position(xalign=0.5,yalign=-0.8)
    play music "audio_hero_911_SIPML_J-0501.mp3"

    narrator "A akhirnya mendatangi istana dan memohon untuk menemui Raja."

    raja "Ada apa seorang anak kecil ingin menemuiku?"

    a "Paduka Raja, maaf atas kelancanganku ini, tetapi aku menemukan banyak pedagang asing di wilayah kita. Sepertinya mereka berasal dari Kerajaan Y, Paduka!"

    raja "Jika itu benar, aku harus segera mengirimkan penjaga kerajaan untuk membubarkan mereka!"

    narrator "Siang hari keesokan harinya, Raja mengirimkan pasukan untuk mengusir para pedagang. Namun, anehnya, pedagang-pedagang tersebut malah mendapatkan dukungan dari warga."

    show citizen_trio_exp
    citizen "Apa yang kalian lakukan?! Mereka menyediakan produk yang lebih baik dibandingkan kalian!"


    narrator "Sikap konsumtif warga menyebabkan Kerajaan X hancur."
    stop music fadeout 1.75
    jump grand_ending_failure


label grand_ending_failure:
    scene bg ruins with fade

    narrator "Kerajaan X kini tinggal reruntuhan, akibat sikap konsumtif rakyatnya. A tersadar bahwa ia kembali ke kelasnya."

    jump classroom_reality

label classroom_reality:
    scene bg classroom with fade
    show a_worried at Position(xalign=0.5,yalign=-0.8)
    play music "audio_hero_HighSchoolGymnasiu+PE375601.mp3"
    a "Bu Guru, Bu Guru, bagaimana nasib Kerajaan X? Apakah mereka menang atau kalah melawan Kerajaan Y?"
    show teacher at Position(xalign=0.0,yalign=-0.8, yoffset=-50)
    g "Haduh, Nak, kamu ini tidak mendengarkan. Kerajaan X kalah akibat konflik internal yang dipicu oleh informasi yang salah."

    a "Pengadu domba?! Bagaimana bisa jadi seperti ini... Aku menyesal atas tindakanku."
    stop music fadeout 1.75
label inform_citizen:
    scene bg market with fade
    play music "Suara rakyat berkerumun.mp3"
    narrator "Untuk menyebarkan desas-desus tersebut, Anthony mendekati para pedagang pasar tradisional dan warga yang berada di lingkungan pasar. Ia kemudian mulai menyebarkan berita tersebut."
    show a_neutral2 at Position(xalign=0.5,yalign=-0.8)
    a "Sejak dulu, warga memang suka bergosip. Mereka adalah penyalur informasi paling cepat! Aku dapat memanfaatkan hal tersebut."
    hide a_neutral2
    show citizen_b_angry with fade

    narrator "Anthony mendekati segerombolan warga yang sedang berbelanja di pasar. Mereka tampak terkejut mendengar berita yang dibawa oleh A."

    citizen_b_angry "Apa benar hal tersebut? Mengerikan sekali! Aku tidak mau membeli dari pasar itu lagi!"

    narrator "Kabar tersebut tersebar luas dengan cepat, hingga Raja X sendiri mendengarnya."

    scene bg palace with fade
    show raja_angry at Position(xalign=0.5,yalign=-0.8)
    raja_marah "Aku harus segera mendatangi lokasi tersebut dan melihat kebenarannya!"
    stop music fadeout 1.75
    jump investigate_market

label investigate_market:
    scene bg market with fade
    play music "Suara rakyat berkerumun.mp3"
    narrator "Raja mendatangi lokasi pasar gedung tersebut dan menggeledah barang-barang yang dijual."
    show raja_angry at Position(xalign=0.5,yalign=-0.8)
    raja "Apa ini?? Siapa kalian?? Beraninya memasuki wilayah kerajaanku!!"

    citizen_b_neutral "Ampuni kami, Yang Mulia! Kami hanya diperintahkan oleh Raja Y untuk berdagang di sini."

    raja "Kurang ajar! Pengawal, gusur mereka sekarang juga! Aku tidak akan membiarkan Kerajaan Y mencuri tanah ini!"
    hide raja_angry with fade
    narrator "Para pedagang digusur, dan warga mulai memboikot produk mereka."

    scene bg palace with fade

    narrator "Raja bertanya pada warga dari mana informasi tersebut berasal, dan warga menunjuk A yang tengah berjalan di pasar."
    show citizen_trio_neutral
    citizen "Kami mengetahuinya dari seorang pemuda itu, Yang Mulia."
    hide citizen_trio_neutral with fade
    stop music fadeout 1.75
    jump palace_recognition

label palace_recognition:
    scene bg palace with fade
    play music "audio_hero_911_SIPML_J-0501.mp3"
    narrator "Seorang ajudan kerajaan diutus untuk mendatangi A."
    show ajudan_salute at Position(xalign=0.0, yalign=-1.0, yoffset=-50)
    ajudan "Raja memanggil seorang anak pemberani yang berhasil membantu kerajaan. Ikutlah denganku ke istana, Le."
    hide ajudan_salute with fade

    show raja_neutral at Position(xalign=0.5,yalign=-0.8)
    raja "Wahai engkau pemuda yang sangat amat berani, aku hargai keberanianmu! Aku berikan gelar Jaka Pradnya Nuraga kepadamu! Sebagai arti bahwa Engkau adalah pemuda yang berani, cerdas, cerdik, dan membantu menyelesaikan masalah!"
    show a_happy2 at Position(xalign=0.0,yalign=-0.8)
    stop music fadeout 1.75
    a "Terimakasih Yang Mulia! Akan ku gunakan gelar ini untuk lebih banyak lagi membantu orang di sekitarku"

    raja "Baguslah, Le. Terapkan itu semua dan ingat-ingat apa yang telah terjadi di Kerajaan ini saat kembali ke tempatmu!!"

    narrator "Anthony merasa aneh, bertanya-tanya mengapa Raja mengetahui tentang asalnya. Namun, sebelum ia sempat berpikir lebih jauh, ia tiba-tiba terbangun."

    jump classroom_final

label classroom_final:
    scene bg classroom with fade
    play music "audio_hero_HighSchoolGymnasiu+PE375601.mp3"
    show a  at Position(xalign=0.0,yalign=-0.8) 
    a "Bu Guru, Bu Guru, bagaimana nasib Kerajaan X? Apakah mereka menang atau kalah melawan Kerajaan Y?"
    show teacher at Position(xalign=0.5,yalign=-0.8)
    g "Haduh, Nak, kamu ini tidak mendengarkan. Kerajaan X menang berkat seorang pemuda bernama Jaka Pradnya Nuraga, yang dengan cerdik membantu kerajaan."

    a "Untunglah... Segala usaha dan pengorbanan tidak sia-sia. Aku akan belajar dari kesalahan Kerajaan X dan berhenti bersikap konsumtif."
    stop music fadeout 1.75


    return

