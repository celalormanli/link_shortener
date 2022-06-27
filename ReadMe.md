# Link Kısaltıcı

Bu projenin amacı verilen linkleri daha kısa linklere dönüştürmek ve oluşturulan yeni linklere gelen istekleri ilgili linklere yönlendirmek. 
### Özellikler
- Verilen link için 10 karakterli bir link uzantısı oluşturmak.
- Kısaltılmış linklere gelen istek sayısını tutmak.
- Kısaltılmış linklere gelen istekleri yönlendirmek.

### Yapı 
- Microservis yapısı kullanılarak oluşturuldu.
- Python üzerinde Django framework'ü kullanılmaktadır.
- Veritanabanı olarak ilişkisel veritabanı kullanılmaktadır.
- Veri tutarlılığı ve servisler arası iletişim için mesaj kuyruk yapısı kullanılmaktadır.

### Kurulum
- web ve admin olarak iki django projesi bulunmaktadır.
- admin ile link yönetimi(link ekleme, listeleme ve gelen istek sayısı) yapılmaktadır.
- web ile kısaltılmış linklere gelen istekler yönetilmektedir.
- Kurulum için iki projede bulunan DATABASES kısmına kullanılacak veritabanı bilgileri girilir. Kuyruk yapısı içinde MQ_URL kısmına gerekli link girlilr.
- Kendim çalıştırırken digitalocean üzerinde bir postgresql veritabanı ile cloudamqp üzerinde rabbitmq kullandım.
- Ayrıca kullanılan sistemde docker kurulu olması beklenmektedir
- Tüm gereksinimler sağlandıktan sonra iki proje içinde aşağıdaki komutlar çalıştırılarak projeler ayağa kaldırılır.

```sh
cd admin
docker-compose build
docker-compose up
```

```sh
cd web
docker-compose build
docker-compose up
```
### Kullanım
- Link Oluşturma - POST -> 0.0.0.0:8000/link/ 
body -> {
    "main_link":"https://www.blabla.com"
}
- Linkleri listeleme - GET -> 0.0.0.0:8000/link/
- Link yönlendirme - GET -> http://0.0.0.0:8001/kısaltma
