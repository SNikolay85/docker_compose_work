# Склады и товары

### Создание и запуск контейнера выполнить командой: 
*docker-compose up -d --build*


Примеры запросов:

@baseUrl = http://localhost:8000/api/v1

```
# поиск складов, где есть определенный продукт
GET {{baseUrl}}/stocks/?search=помид
Content-Type: application/json
```
```
# создание продукта
POST {{baseUrl}}/products/
Content-Type: application/json

{
  "title": "Огурец",
  "description": "Лучшие огурцы"
}
```
```
# получение всех продуктов
GET {{baseUrl}}/products/
Content-Type: application/json
```
```
# получение продуктов по определенному полю
GET {{baseUrl}}/products/?stock=1
Content-Type: application/json
```
```
# поиск продуктов по значению поля
GET {{baseUrl}}/products/?q='зелень'
Content-Type: application/json
```
```
# упорядочивание продуктов по полям
GET {{baseUrl}}/products/?o=-id,title
Content-Type: application/json
```
```
# обновление продукта
PATCH {{baseUrl}}/products/4/
Content-Type: application/json

{
  "description": "Самая свежая зелень"
}
```
```
# удаление продукта
DELETE {{baseUrl}}/products/1/
Content-Type: application/json
```
```
# поиск продуктов по названию и описанию
GET {{baseUrl}}/products/?search=помидор
Content-Type: application/json
```
```
# создание склада
POST {{baseUrl}}/stocks/
Content-Type: application/json

{
  "address": "мой адрес не дом и не улица, мой адрес сегодня такой: www.ленинград-спб.ru3",
  "positions": [
    {
      "product": 2,
      "quantity": 250,
      "price": 120.50
    },
    {
      "product": 3,
      "quantity": 100,
      "price": 180
    }
  ]
}
```
```
# обновляем записи на складе
PATCH {{baseUrl}}/stocks/4/
Content-Type: application/json

{
  "positions": [
    {
      "product": 2,
      "quantity": 100,
      "price": 130.80
    },
    {
      "product": 3,
      "quantity": 243,
      "price": 145
    }
  ]
}
```
```
# поиск складов, где есть определенный продукт
GET {{baseUrl}}/stocks/?products=2
Content-Type: application/json