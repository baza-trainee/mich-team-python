/api/cart – кошик користувача. Для зареєстрованого користувача працює на основі Token, для не зареєстрованого на основі sessions. Надаються автоматично.

GET:
якщо кошик порожній повертає:
{"cart_items": [],"total_items": 0}

якщо користувач не зареєстрований але додав товар до кошика (автоматично надається Cookie приклад: sessionid=nein2y64i2moz5r48igvvx47i0rjdtyw):
{"cart_items": [{"id": 174,"session_id": "nein2y64i2moz5r48igvvx47i0rjdtyw","size": "M","quantity": 1,"is_active": true,"user": null,"product": 2,"Order": null}],"total_items": 1}

якщо користувач зареєстрований, додав товар у кошик (Поле User присвоюється відповідному користувачеві на основі токена переданого в headers, так само автоматично надається Cookie приклад: sessionid=nein2y64i2moz5r48igvvx47i0rjdtyw):{"cart_items": [{"id": 177,"session_id": "nxbjveeqxrxwjz0rfjhco6mkrkjywh4d","size": "M","quantity": 1,"is_active": true,"user": 1,"product": 2,"Order": null}],"total_items": 1}

POST:

для додавання товару до кошика:product - обов'язкове поле, що передає id продуктуquantity - не обов'язкове поле, вказує на кількість товару, якщо не передавати, то default=1size - обов'язкове поле, що вказує на розмір, товари без розміру вказуються як NS (No Size)


PUT:для зміни товару:для зміни кількості товару необхідно передати product, quantity, size для зміни розміру товару 
необхідно передати product, size, new_size


якщо розмір не існує, повертається:
{"error": "Invalid new_size for the product"}

якщо розмір існує, повертається (JSON із зміненим товаром):
{"id": 177,"session_id": "nxbjveeqxrxwjz0rfjhco6mkrkjywh4d","size": "L","quantity": 1,"is_active": true,"user": 1,"product": 2,"Order": null}

якщо товару не існує:
{"error": "Product not found"}

DELETE:
Видалення товару з кошика


якщо товару немає, повертається:
{"error": "Cart item not found"}

якщо товар існує, повертається:
{"message": "Cart item deleted successfully"}