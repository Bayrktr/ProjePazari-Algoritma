Proje Pazari icin hazirladigim projenin algoritma kismi

Oncelik Sirasi:
1-Stok 
2-Kullanici talepleri
3-Talep gören kategori

-Uygulamaya çalıştığım şey görünürde basit fakat biraz açıklayınca ne boyutta olduğunu anliyacaksiniz.
-Öncelikle haliyle daha önce toplamiş olduğumuz bazı veriler var bunları değerlendirmemiz gerekiyor.Bir kayıt içerisinde alışverişi yapan kişi, nerde yaptığı ve ne aldığı ve kaç adet aldığı gibi önemli veriler var öncelikle menüsü hazırlanıcak kişinin önceki verilerini sistem çekiyor ve iki tane büyük liste oluşturuyor bunlar geçmişte alınan ürünler ve kaç tane alındıkları birinci listede öncelikle farklı elemanların bulunması gerekiyor örnek vericek olursak elimizde 14 elemanlı bir liste var fakat sadece 3 tane farklı eleman var ve bu elemanlar düzensiz bir şekilde tekrarlıyor bizim farklı elemanları bulup bir liste içine atmamız gerekiyorki ilerde index numarası araması yaparken işimize yarasınlar.Bu işlemi yaptıktan sonra liste içerisindeki elemanların daha önce bahsettiğim ikinci büyük listede index numaraları bulunuyor böylece her üründen geçmişte toplamda kaç tane alındığı bulunmuş oluyor.Sonrasında bu veriye göre bir algoritma yazılıyor.Onu ben bilsem yeter .d 
-Ayrıyeten bazı testler yapılması gerekiyordu bunun için bazı programlar yazdım onlar sayesinde her seferinde farklı durumların olduğu simulasyonlar yaratabildim.Aynı zamanda zaman tasarrufu sağlıyorlar.
-Güncelleme(16.04.2022)
En sevilen ürününe indirim uygulamayı unutmuşum onu ekledim indirim uygulandıktan sonra olusan float değerini eğer oluştuysa int a çevirme ekledim kısaca ondalıklı sayıdan kurtuldum bu kadar .d 
-Guncelleme(20.04.2022) 
En sevilen kategorilerin belirlenmesini sağladım bu kategorilerin kamu üzerinde sevilenden sevilmeyen olucak şekilde sıralamasını sağladım
Sonrasında her kategori ekrana basildiktan sonra bu kategoriye ait ürünler sevilenden sevilmeyene olucak şekilde sıralandı.
Bazı istisnaları test etmem lazım boş kategoriler kategorisiz(None) ürünler gibi bu gibi durumlar gerçekleştiğinde programda error veriyor error ayıklama ile alakalı birşey eklenebilir .
-Güncelleme(29.04.2022)
Menülerin kişiselleştirilmesi üzerinde duruyorum sistem üzerinden font,title;tek satırdaki eleman sayısı,tek satırdaki elemanların aralık boyutları,alt satırdaki eleman ile mesafe gibi özellikler ayarlanıcak.Bu boyutların menü üzerinde kapladığı yere göre ek sayfa açılacak sayfalar ihtiyaç kadar algoritma tarafından açılacak.Ve ayrıyeten algoritmadaki bir sorunu giderdim sorun yüzünden sadece belli ürünlerin alım sayıları değerlendirilebiliyordu gereksiz bir koşulu kaldırdım ve bingo .d
Ek Not: Bir fikir önerisi aldım,kişiye önerilecek yemekler besin değerleri ve kişinin sağlık durumuna göre ayarlanıcak beta sürümünü hazırladıktan uğraşıcam.
-Güncelleme(04.05.2022)
Önceki güncellemede bahsettiğim işletmelerin menüleri kişiselleştirebilmesini sisteme ekledim admin panelinden istenilen özellikler giriliyor ve menü ona göre şekilleniyor ve ayriyeten menü üzerinde bulunan ileri geri butonları artık belirlenen pencere boyutlarına oranlı bir şekilde oluşuyor(width/10,height/20),stok kontrolü ve indirim üzerinde yoğunlaşıcam indirim konusunu zaten yapmıştım ama biraz geliştiricem ve stok kontrolünü kafamı karıştırdığı için iptal etmiştim ona bir el atıcam sisteme stok kontrolü ve indirim özelliklerini belirleme özelliği eklicem bu sayede işletme bu işleri düzenleyebilecek.
