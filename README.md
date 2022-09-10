# API- System booking api


Create a minimal project (inspired by instagram) in Django.

## Features
- <br>
- <br>
- <br>
- <br>
- Counter of followers for each user<br>

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
docker-compose build
docker-compose run web python manage.py makemigrations api
docker-compose run web python manage.py migrate api
```

## API

### Client

#### /client  

- `POST` : Create One Client
- `GET`  : Get All Client

#### /client/:id

- `GET` : Get One Client 
- `PATCH`: Update Partial One Client
- `PUT` : Update One Client 
- `DELETE` : Delete One Client

### Room

#### /room  

- `POST` : Create One Room
- `GET`  : Get All Room

#### /room/:id

- `GET` : Get One Room 
- `PATCH`: Update Partial One Room
- `PUT` : Update One Room 
- `DELETE` : Delete One Room

### Payment Method

#### /paymentmethod  

- `POST` : Create One Payment Method
- `GET`  : Get All Payment Method

#### /paymentmethod/:id

- `GET` : Get One Payment Method 
- `PATCH`: Update Partial One Payment Method
- `PUT` : Update One Payment Method 
- `DELETE` : Delete One Payment Method

### Invoice

#### /invoice  

- `POST` : Create One Invoice
- `GET`  : Get All Invoice

#### /invoice/:id

- `GET` : Get One Invoice 
- `PATCH`: Update Partial One Invoice
- `PUT` : Update One Invoice 
- `DELETE` : Delete One Invoice

### Booking

#### /booking  

- `POST` : Create One Booking
- `GET`  : Get All Booking

#### /invobookingice/:id

- `GET` : Get One Booking 
- `PATCH`: Update Partial One Booking
- `PUT` : Update One Booking 
- `DELETE` : Delete One Booking

## License
[This project is under MIT License](https://opensource.org/licenses/MIT)

## Author
[Franco Roca](https://github.com/francoxr) | 2021