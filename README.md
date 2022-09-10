# API- System booking api

Create an api for system booking in Django.

## Technologies
- Python
- Django
- Django Rest Framework
- PostgreSQL
- Docker
- Docker Compose

## Dependencies
Python<br>
Django<br>
Django Rest Framework<br>
psycopg2<br>

## Usage

```
git clone 
docker-compose up
docker-compose run web python manage.py makemigrations api
docker-compose run web python manage.py migrate api
```


# Nota

Dentro de este readme , se encuentra ejemplos de la API en la seccion API. Ademas adjunto un archivo llamado Documentation , el cual brinda mas detalles acerca de la aplicacion y del flujo

# API

## Client

#### api/v1/client/create  

- `POST` : Create One Client

Request body:

```
{
    "name": "Franco",
    "last_name": "Roca",
    "email": "frsR@gmail.com",
    "phone": "985632478"
}
```

#### api/v1/client  

- `GET`  : Get All Client

Response body:

```
[
    {
        "id": 4,
        "name": "Alvar",
        "last_name": "fernasd",
        "email": "Alvar@gmai.com",
        "phone": 985632132,
        "is_company": false,
        "created": "2022-09-10T03:10:18.878172Z",
        "modified": "2022-09-10T03:10:18.878189Z"
    },
    {
        "id": 5,
        "name": "Bari",
        "last_name": "Bernal",
        "email": "Bari@gmai.com",
        "phone": 985664132,
        "is_company": false,
        "created": "2022-09-10T03:10:44.866211Z",
        "modified": "2022-09-10T03:10:44.866232Z"
    }
]
```

#### api/v1/client/:id

- `GET` : Get One Client 

Response body:

```
{
    "id": 4,
    "name": "Alvar",
    "last_name": "fernasd",
    "email": "Alvar@gmai.com",
    "phone": 985632132,
    "is_company": false,
    "created": "2022-09-10T03:10:18.878172Z",
    "modified": "2022-09-10T03:10:18.878189Z"
}
```

#### api/v1/client/:id/update

- `PATCH`: Update Partial One Client

Request body:

```
{
    "name": "Alvare",
    "last_name": "herrorge"
}

```

- `PUT` : Update One Client 

Request body:

```
{
    "name": "Alvare",
    "last_name": "herrorge"
    "email": "Alvarda@gmai.com",
    "phone": 983432132,
}

```

#### api/v1/client/:id/delete

- `DELETE` : Delete One Client

Response body:

```
{
    "message": "Cliente Eliminado Correctamente"
}
```
## Room

#### api/v1/room/create  

- `POST` : Create One Room

Request body:

```
{
    "code" : "201",
    "detail": "por reparar"
}
```

#### api/v1/room  

- `GET`  : Get All Room

Response body:

```
[
    {
        "id": 1,
        "code": "101",
        "detail": "nuevo",
        "created": "2022-09-10T18:24:43.337858Z",
        "modified": "2022-09-10T18:24:43.337875Z"
    },
    {
        "id": 2,
        "code": "102",
        "detail": "nuevo",
        "created": "2022-09-10T18:24:57.687832Z",
        "modified": "2022-09-10T18:24:57.687858Z"
    },
    {
        "id": 3,
        "code": "103",
        "detail": "por reparar",
        "created": "2022-09-10T18:25:04.538745Z",
        "modified": "2022-09-10T18:25:04.538768Z"
    }
]
```

#### api/v1/room/:id

- `GET` : Get One Room 

Response body:

```
{
    "id": 3,
    "code": "103",
    "detail": "por reparar",
    "created": "2022-09-10T18:25:04.538745Z",
    "modified": "2022-09-10T18:25:04.538768Z"
}
```

#### api/v1/room/:id/update

- `PATCH`: Update Partial One Room

Request body:

```
{
    "detail": "reparado"
}

```

- `PUT` : Update One Room 

Request body:

```
{
    "code": "202",
    "detail": "reparado"
}

```

#### api/v1/room/:id/delete

- `DELETE` : Delete One Room

Response body:

```
{
    "message": "Cuarto Eliminado Correctamente"
}
```

## Payment Method

#### api/v1/paymentmethod/create  

- `POST` : Create One Payment Method

Request body:

```
{
    "name": "tarjeta de Debito"
}
```

#### api/v1/paymentmethod  

- `GET`  : Get All Payment Method

Response body:

```
[
    {
        "id": 2,
        "name": "efectivo",
        "created": "2022-09-10T18:32:06.472778Z",
        "modified": "2022-09-10T18:32:06.472797Z"
    },
    {
        "id": 3,
        "name": "tarjeta de credito",
        "created": "2022-09-10T18:32:13.987475Z",
        "modified": "2022-09-10T18:32:13.987495Z"
    }
]
```

#### api/v1/paymentmethod/:id

- `GET` : Get One Payment Method 

Response body:

```
{
    "id": 2,
    "name": "efectivo",
    "created": "2022-09-10T18:32:06.472778Z",
    "modified": "2022-09-10T18:32:06.472797Z"
}
```

#### api/v1/paymentmethod/:id/update

- `PATCH`: Update Partial One Payment Method

Request body:

```
{
    "name": "tarjeta de Debito"
}
```

- `PUT` : Update One Payment Method 

Request body:

```
{
    "name": "tarjeta de Debito"
}
```


#### api/v1/paymentmethod/:id/delete

- `DELETE` : Delete One Payment Method

Response body:

```
{
    "message": "Metodo de Pago Eliminado Correctamente"
}
```

## Invoice

#### api/v1/invoice/create  

- `POST` : Create One Invoice

Request body:

```
{
    "name" : "F001",
    "detail": "familia",
    "amount_payed": 350,
    "client": 4,
    "payment_method": 2
}
```

#### api/v1/invoice  

- `GET`  : Get All Invoice

Response body:

```
[
    {
        "id": 1,
        "name": "F001",
        "detail": "familia",
        "amount_payed": 350,
        "created": "2022-09-10T19:05:39.071315Z",
        "modified": "2022-09-10T19:05:39.071329Z",
        "client": 4,
        "payment_method": 2
    }
]
```

#### api/v1/invoice/:id

- `GET` : Get One Invoice 

Response body:

```
{
    "id": 1,
    "name": "F001",
    "detail": "familia",
    "amount_payed": 350,
    "created": "2022-09-10T19:05:39.071315Z",
    "modified": "2022-09-10T19:05:39.071329Z",
    "client": 4,
    "payment_method": 2
}
```

#### api/v1/invoice/:id/update

- `PATCH`: Update Partial One Invoice

Request body:

```
{
    "name" : "F0012",
}
```

- `PUT` : Update One Invoice

Request body:

```
{
    "name" : "F00132",
    "detail": "pareja",
    "amount_payed": 456,
    "client": 4,
    "payment_method": 2
}
```

#### api/v1/invoice/:id/delete

- `DELETE` : Delete One Invoice

Response body:

```
{
    "message": "Factura Eliminado Correctamente"
}
```

## Booking

#### api/v1/booking/create  

- `POST` : Create One Booking

Request body:

```
{
    "date_start": "2022-08-15",
    "date_end": "2022-08-20",
    "day_stay": 6,
    "room": 2
}
```

#### api/v1/booking  

- `GET`  : Get All Booking

Response body:

```
[
    {
        "id": 1,
        "date_start": "2022-08-15",
        "date_end": "2022-08-20",
        "day_stay": 6,
        "state": "PE",
        "created": "2022-09-10T19:12:34.540002Z",
        "modified": "2022-09-10T19:12:34.540013Z",
        "room": 2,
        "invoice": null
    }
]
```

#### api/v1/booking/:id

- `GET` : Get One Booking 

Response body:

```
{
    "id": 1,
    "date_start": "2022-08-15",
    "date_end": "2022-08-20",
    "day_stay": 6,
    "state": "PE",
    "created": "2022-09-10T19:12:34.540002Z",
    "modified": "2022-09-10T19:12:34.540013Z",
    "room": 2,
    "invoice": null
}
```

#### api/v1/booking/:id/update

- `PATCH`: Update Partial One Booking

Request body:

```
{
    "room": 3
}
```

- `PUT` : Update One Booking

Request body:

```
{
    "date_start": "2022-08-15",
    "date_end": "2022-08-22",
    "day_stay": 8,
    "room": 3
}
```

#### api/v1/booking/:id/delete

- `DELETE` : Delete One Booking

Response body:

```
{
    "message": "Reservacion Eliminado Correctamente"
}
```

## License
[This project is under MIT License](https://opensource.org/licenses/MIT)

## Author
[Franco Roca](https://github.com/francoxr) | 2022