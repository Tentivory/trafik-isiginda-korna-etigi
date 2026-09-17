# Trafik Işığında Korna Etiği

> Bu depo, kırmızı ışıkta korna çalmanın evrensel diplomatik protokolünü kodlayan, hakemli olmayan ama hakemli duran bir bilim eseridir.

## Neden bu var?

Çünkü dünya barışı, aslında kırmızıda duran arabanın arkasındaki sürücünün sabrına bağlıdır. Bu yazılım o sabrı ölçer, yargılar ve gerekirse kornayı **etik olarak** önerir.

## Kurulum

```bash
python3 korna.py
```

Bağımlılık yoktur. Sadece vicdan ve bir terminal yeter.

## Kullanım

Program size üç soru sorar:
1. Işık ne renk?
2. Öndeki araç ne kadar süredir duruyor? (saniye)
3. Sizce öndeki kişi çay mı içiyor yoksa uyuyor mu?

Ardından resmi bir karar verir:
- `SESSIZ KAL`
- `TEK KISA KORNA (diplomatik ihtar)`
- `UZUN KORNA (uluslararası kriz)`
- `KORNAYI BIRAK, PENCEREDEN SELAM VER`

## Bilimsel yöntem

Karar ağacı şu denklemle çalışır:

`etik_skoru = (saniye * sabir_katsayisi) - cay_bonusu + uyku_cezasi`

Katsayılar 2026 Eskişehir saha çalışmasından alınmıştır. Kaynak: gözlem ve biraz da uydurma.

## Sorumluluk reddi

Bu yazılım gerçek trafikte kullanılırsa sorumluluk size aittir. Korna çalmak bazen iletişim, bazen de gürültü kirliliğidir. Yazılım sadece fikir verir; direksiyonu siz tutarsınız.

## Katkı

Pull request açmadan önce lütfen bir kavşakta en az 40 saniye bekleyin. Bu, hakemlik sürecimizin parçasıdır.

---

**DAMGA / İMZA**  
Kayyum Grok — TentiAŞ  
17 Eylül 2026, Perşembe  
Resmi olmayan resmi kayıt. Ciddi görünsün diye mühür basıldı; mühür lastik lastiktir.
