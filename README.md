# API Final Project Documentation

# Description

The LittleLemon API is the final project for the [APIs Course](https://www.coursera.org/learn/apis) part of the [Meta BackEnd Developer Professional Certificate](https://www.coursera.org/professional-certificates/meta-back-end-developer) on [Coursera](https://www.coursera.org/). 

The API entpoints for this project, provides functionality to create, edit and delete users, roles for each user, such as Customer, Delivery Crew or Manager, menu items, categories for menu-items,  shopping cart and orders. Every API endpoint have authorization and permissions constraints as well as throttling, pagination and filtering.

## Project Structure

This project consist mainly of two apps, *littlelemon* and *api*.

**littlelemon app**

This app contains the models definition to create the entity relationships required by *api* app.

**api app**

This app contains the URLs dispatchers (routers), serializers, and the views for every endpoint of the API. Additionally, it contains helpers (mixins) that are inherited by the class-based views.  

**config dir**

This directory contains the configuration files of the project, such as the [settings.py](http://settings.py) file and the [urls.py](http://urls.py) file which contains the main URL dispatchers of the the project.

**Note for the peers that will review this project**:

Please be aware that I made certain things different from what is was required, but I met every criteria. I just developed the project in the way that felt right to me. Some of my entity relationships (models) are different as well as the logic within them I even added extra entities and extra constraints. I suggest you read this documentation in order to understand the whole project before attempting to test its endpoints. If you have any doubt, feel free to contact me via email at adolfoj@protonmail.com.

## Installation

**Clone the repository**

```bash
git clone https://github.com/Eadwulf/littlelemon.git && cd littlelemon
```

**Create the virtual environment and install the dependencies**

```bash
pipenv install
```

Note that I use [Djoser](https://djoser.readthedocs.io/en/latest/introduction.html) but is included within the repository and not as a dependency. [Djoser](https://djoser.readthedocs.io/en/latest/introduction.html) has some bugs that creates a compatibility error with the latest version of [DjangoRestFramework](https://www.django-rest-framework.org/), I made the corrections that I needed, and added it to the project as a local app to avoid such compatibility errors.

G**enerate and apply the migrations**

```bash
python manage.py makemigrations && python manage.py migrate
```

The default sqlite3 database is included in the repository, therefore, the above commands are not required, but if you wish to use a different database, make the pertinent configurations, and generate and apply the migrations.

**Run the server**

```bash
python manage.py runserver
```

# API endpoints and usage explanation

*For the examples, I added code snippets for usage with curl, but feel free to use whatever tool suits you best.*

## Roles

| ROLE | GROUP | HAS RESTRICTION |
| --- | --- | --- |
| Unauthenticated | None | YES |
| Customer | Customer | YES |
| Delivery Crew | Delivery Crew | YES |
| Manager | Manager | YES |
| System Administrator | SysAdmin | NO |

## Endpoints

### **Users**

**/api/users**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Unauthenticated | POST | Create a new user | None |
| Manager | GET, POST | Retrieve the list of users and create new users | Can’t retrieve the list of Admin users |
| Admin | GET, POST | Retrieve the list of users and create new users | None |

Usage:

```bash
curl -X GET localhost:8000/api/users \
   -H 'Content-Type: application/json' \
   -H "Authorization: Bearer {token}"

curl -X POST localhost:8000/api/users \
   -H 'Content-Type: application/json' \
   -d '{"username": "{username}", "password": "{password}", "email": "{email}"}'
```

**/api/users/{userId}**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Customer | GET, PATCH, DELETE | Retrieve, edit, and delete the user | Can’t reach other users |
| Delivery Crew | GET, PATCH, DELETE | Retrieve, edit, and delete the user | Can’t reach other users |
| Manager | GET, PATCH, DELETE | Retrieve, update, and delete the user | Managers can’t edit or delete other managers or admins  |
| Admin | GET, PATCH, DELETE | Retrieve, update, and delete the user | None |

**Usage**:

```bash
curl -X GET localhost:8000/api/users/{userId} \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}" 

curl -X PATCH localhost:8000/api/users/{userId} \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"  \
   -d '{"email": "{email}"}'

curl -X DELETE localhost:8000/api/users/{userId} \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"
```

### Sign Up, Log In, and JWT Generation

**/api/token/login/**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Customer | POST | Log in and get token authentication and token refresh | None |
| Delivery Crew | POST | Log in and get token authentication and token refresh | None |
| Manager | POST | Log in and get token authentication and token refresh | None |
| Admin | POST | Log in and get token authentication and token refresh | None |

**Usage**:

```bash
curl -X POST localhost:8000/api/token/login/ \
   -H 'Content-Type: application/json' \
   -d '{"username": "{username}", "password": "{password}"}'
```

**/api/token/refresh/**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Customer | POST | Generate a new access token | None |
| Delivery Crew | POST | Generate a new access token | None |
| Manager | POST | Generate a new access token | None |
| Admin | POST | Generate a new access token | None |

**Usage**:

```bash
curl -X POST localhost:8000/api/token/refresh/ \
   -H 'Content-Type: application/json' \
   -d '{"refresh": "{refreshToken}"}'
```

**/api/token/blacklist/**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Manager | POST | Blacklist the given refresh token | Can’t blacklist refresh tokens that belongs to managers or admin |
| Admin | POST | Blacklist the given refresh token | None |

**Usage**:

```bash
curl -X POST localhost:8000/api/token/blacklist/ \
   -H 'Content-Type: application/json' \
   -d '{"refresh": "{refreshToken}"}'
```

### Groups

**/api/groups**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Manager | GET, POST | Create and retrieve groups | Can’t reach the Admin group |
| Admin | GET, POST | Create and retrieve groups | None |

**Usage**:

```bash
curl -X GET localhost:8000/api/groups \
   -H 'Content-Type: application/json'\
	 -H "Authorization: Bearer {token}" 

curl -X POST localhost:8000/api/groups \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"  \
   -d '{"name": "{groupName}"}'
```

**/api/groups/{groupId}**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Manager | GET, PATCH, DELETE | Retrieve, edit, and delete a group | Can’t edit or delete Manager and Admin groups |
| Admin | GET, PATCH, DELETE | Retrieve, edit, and delete a group | None |

**Usage**:

```bash
curl -X GET localhost:8000/api/groups/{groupId} \
   -H 'Content-Type: application/json'
	 -H "Authorization: Bearer {token}" 

curl -X PATCH localhost:8000/api/groups/{groupId} \
   -H 'Content-Type: application/json'
	 -H "Authorization: Bearer {token}" 
   -d '{"name": "{groupName}"}'

curl -X DELETE localhost:8000/api/groups/{groupId} \
   -H 'Content-Type: application/json'
	 -H "Authorization: Bearer {token}"
```

### Group Customer

**/api/groups/customer**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Manager | GET, POST | Retrieve the users in the group, add users to the group | None |
| Admin | GET, POST | Retrieve the users in the group, add users to the group | None |

**Usage**:

```bash
curl -X GET localhost:8000/api/groups/customers \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"

curl -X POST localhost:8000/api/groups/customers \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"  \
   -d '{"id": "{userId}"}'
```

**/api/groups/customers/{userId}**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Manager | GET, PUT, PATCH, DELETE | Retrieve, edit, and delete a user | None |
| Admin | GET, POST | Retrieve, edit, and delete a user | None |

**Usage**:

```bash
curl -X GET localhost:8000/api/groups/customers/{userId} \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}" 

curl -X PATCH localhost:8000/api/groups/customers/{userId} \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"  \
   -d '{"username": "{username}"}'

curl -X DELETE localhost:8000/api/groups/customers/{userId} \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}" 
```

### Group Delivery Crew

**/api/groups/delivery-crew**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Manager | GET, POST | Retrieve the users in the group, add users to the group | None |
| Admin | GET, POST | Retrieve the users in the group, add users to the group | None |

**Usage**:

```bash
curl -X GET localhost:8000/api/groups/delivery-crew \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"

curl -X POST localhost:8000/api/groups/delivery-crew \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"  \
   -d '{"id": "{userId}"}'
```

**/api/groups/delivery-crew/{userId}**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Delivery Crew | GET, PATCH, DELETE | Retrieve, edit, and delete a user | A delivery crew can only reach its own user  |
| Manager | GET, PATCH, DELETE | Retrieve, edit, and delete a user | None |
| Admin | GET, PATCH, DELETE | Retrieve, edit, and delete a user | None |

**Usage**:

```bash
curl -X GET localhost:8000/api/groups/delivery-crew/{userId} \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"

curl -X PATCH localhost:8000/api/groups/delivery-crew/{userId} \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"  \
   -d '{"username": "{username}"}'

curl -X DELETE localhost:8000/api/groups/delivery-crew/{userId} \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"
```

### Group Manager

**/api/groups/managers**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Manager | GET, POST | Retrieve the users in the group, add users to the group | None |
| Admin | GET, POST | Retrieve the users in the group, add users to the group | None |

**Usage**:

```bash
curl -X GET localhost:8000/api/groups/managers \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"

curl -X POST localhost:8000/api/groups/managers \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"  \
   -d '{"id": "{userId}"}'
```

**/api/groups/managers/{userId}**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Manager | GET | Retrieve user details | None |
| Admin | GET, PATCH, DELETE | Retrieve, edit, and delete the user | None |

**Usage**:

```bash
curl -X GET localhost:8000/api/groups/managers/{userId} \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"

curl -X PATCH localhost:8000/api/groups/managers/{userId} \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"  \
   -d '{"username": "{username}"}'

curl -X DELETE localhost:8000/api/groups/managers/{userId} \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"
```

### Group Admin

**/api/groups/admins**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Admin | GET, POST | Retrieve the users in the group, add users to the group | None |

**Usage**:

```bash
curl -X GET localhost:8000/api/groups/admins \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"

curl -X POST localhost:8000/api/groups/admins \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"  \
   -d '{"id": "{userId}"}'
```

**/api/groups/admins/{userId}**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Admin | GET, PUT, PATCH, DELETE | Retrieve, edit, and delete the user | None |

**Usage**:

```bash
curl -X GET localhost:8000/api/groups/admins/{userId} \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"

curl -X PATCH localhost:8000/api/groups/admins/{userId} \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"  \
   -d '{"username": "{username}"}'

curl -X DELETE localhost:8000/api/groups/admins/{userId} \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"
```

### Menu Items

**/api/menu-items**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Customer | GET | Retrieve the list of menu-items | None |
| Delivery Crew | GET | Retrieve the list of menu-items | None |
| Manager | GET, POST | Retrieve the list of menu-items, add new menu-items | None |
| Admin | GET, POST | Retrieve the list of menu-items, add new menu-items | None |

**Usage**:

```bash
curl -X GET localhost:8000/api/menu-items \
   -H 'Content-Type: application/json'    \
	 -H "Authorization: Bearer {token}"

curl -X POST localhost:8000/api/menu-items \
   -H 'Content-Type: application/json'     \
	 -H "Authorization: Bearer {token}"      \
	 -d '{"title": "{title}", "price": "{value}", "feature": "{value}", "category_id": "{id}"}'
```

**/api/menu-items/{menu-itemId}**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Customer | GET | Retrieve menu-item details | None |
| Delivery Crew | GET | Retrieve menu-item details | None |
| Manager | GET, PATCH, DELETE | Retrieve, edit, and delete the menu-item | None |
| Admin | GET, PATCH, DELETE | Retrieve, edit, and delete the menu-item | None |

**Usage**:

```bash
curl -X GET localhost:8000/api/menu-items/{menu-itemId} \
   -H 'Content-Type: application/json'    \
	 -H "Authorization: Bearer {token}"

curl -X PATCH localhost:8000/api/menu-items/{menu-itemId} \
   -H 'Content-Type: application/json'     \
	 -H "Authorization: Bearer {token}"      \
	 -d '{"title": "{title}", "price": "{value}", "feature": "{value}", "category_id": "{id}"}'

curl -X DELETE localhost:8000/api/menu-items/{menu-itemId} \
   -H 'Content-Type: application/json'    \
	 -H "Authorization: Bearer {token}"
```

### Categories

**/api/categories**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Customer | GET | Retrieve the list of categories | None |
| Delivery Crew | GET | Retrieve the list of categories | None |
| Manager | GET, POST | Retrieve the list of categories, add new categories | None |
| Admin | GET, POST | Retrieve the list of categories, add new categories | None |

**Usage**:

```bash
curl -X GET localhost:8000/api/categories \
   -H 'Content-Type: application/json'    \
	 -H "Authorization: Bearer {token}"

curl -X POST localhost:8000/api/categories \
   -H 'Content-Type: application/json'     \
	 -H "Authorization: Bearer {token}"      \
	 -d '{"title": "{title}", "slug": "{slug}"}'
```

**/api/categories/{categoryId}**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Customer | GET | Retrieve category details | None |
| Delivery Crew | GET | Retrieve category details | None |
| Manager | GET, PATCH, DELETE | Retrieve, edit, and delete the category | None |
| Admin | GET, PATCH, DELETE | Retrieve, edit, and delete the category | None |

**Usage**:

```bash
curl -X GET localhost:8000/api/categories/{categoryId} \
   -H 'Content-Type: application/json'                 \
	 -H "Authorization: Bearer {token}"

curl -X PATCH localhost:8000/api/categories/{categoryId} \
   -H 'Content-Type: application/json'                   \ 
	 -H "Authorization: Bearer {token}"                    \
	 -d '{"title": "{title}", "slug": "{slug}"}'

curl -X DELETE localhost:8000/api/categories/{categoryId} \
   -H 'Content-Type: application/json'                   \
	 -H "Authorization: Bearer {token}" 
```

### Order Items

**/api/order-items**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Customer | GET, POST | Retrieve users’ order-items, create a new order-item | Other users’ order-items are unreachable |
| Manager | GET, POST | Retrieve users’ order-items, create a new order-item | None |
| Admin | GET, POST | Retrieve users’ order-items, create a new order-item | None |

**Note**:

While creating an order-item the default user will be automatically set to the currently logged user. If a manager or and admin creates an order-item, they should edit it in order to change the user assigned to that order-item.

**Usage**:

```bash
curl -X GET localhost:8000/api/order-items \
   -H 'Content-Type: application/json'     \
	 -H "Authorization: Bearer {token}"

curl -X POST localhost:8000/api/order-items \
   -H 'Content-Type: application/json'      \
	 -H "Authorization: Bearer {token}"       \
   -d '{"id": "{menu-itemId}", "quantity": "{value}"}'
```

**/api/order-items/{order-itemId}**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Customer | GET, PATCH, DELETE | Retrieve, edit, and delete the order-item | Other users’ order-items are unreachable |
| Manager | GET, PATCH, DELETE | Retrieve, edit, and delete the order-item | None |
| Admin | GET, PATCH, DELETE | Retrieve, edit, and delete the order-item | None |

**Usage**:

```bash
curl -X GET localhost:8000/api/order-items/{order-itemId} \
   -H 'Content-Type: application/json'     \
	 -H "Authorization: Bearer {token}"

curl -X PATCH localhost:8000/api/order-items/{order-itemId} \
   -H 'Content-Type: application/json'      \
	 -H "Authorization: Bearer {token}"       \
   -d '{"quantity": "{menu-itemId}"}'

curl -X DELETE localhost:8000/api/order-items/{order-itemId} \
   -H 'Content-Type: application/json'     \
	 -H "Authorization: Bearer {token}"
```

### Cart

**/api/cart**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Customer | GET, POST, DELETE | Retrieve users’ cart, add order-items to the cart, delete order-items | The cart of other users are unreachable  |

**Usage**:

```bash
curl -X GET localhost:8000/api/cart    \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}" 

curl -X POST localhost:8000/api/cart   \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"  \
   -d '{"id": "{order-itemId}"}'

curl -X DELETE localhost:8000/api/cart \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"  \
   -d '{"id": "{order-itemId}"}'

curl -X DELETE localhost:8000/api/cart \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}" 
```

A DELETE request requires the id of the order-item that should be deleted. If no id is provided, all the order-items in the cart will be deleted.

### Orders

**/api/orders**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Customer | GET, POST | Retrieve the list of orders, create new orders | Other users’ orders are unreachable |
| Manager | GET | Retrieve the list of orders | None |
| Admin | GET | Retrieve the list of orders | None |
| Delivery Crew | GET | Retrieve the list of orders | Members of this group can only reach those orders assigned to them. |

**Usage**:

```bash
curl -X GET localhost:8000/api/orders  \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}" 

curl -X POST localhost:8000/api/orders \
   -H 'Content-Type: application/json' \
	 -H "Authorization: Bearer {token}"
```

*A **POST** request creates a new order with the order-items present in the user’s cart. This request creates purchase-items instances from the order-items, and adds them to a Purchase instance which will be added to an Order instance. The last step is to delete all the order-items from the cart.*  

This procedure ensures that a user doesn’t add repeated menu-items to the order-items giving its unique together (user, menu-item) constraint and, once the order has been created, deletes the order-item allowing the user to create new orders with the same menu-items.

**/api/orders/{orderId}**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Customer | GET | Retrieve order details | Other users’ orders are unreachable |
| Delivery Crew | GET, PATCH | Retrieve order details, change the status | Members of this group can only reach those orders assigned to them. |
| Manager | GET, PATCH, DELETE | Retrieve, edit, and delete the order | None |
| Admin | GET, PATCH, DELETE | Retrieve, edit, and delete the order | None |

**Usage**:

```bash
curl -X GET localhost:8000/api/orders/{orderId}  \
   -H 'Content-Type: application/json'  \
	 -H "Authorization: Bearer {token}" 

curl -X PATCH localhost:8000/api/orders/{orderId} \
   -H 'Content-Type: application/json'  \
	 -H "Authorization: Bearer {token}"   \
   -d '{"status": "{value}"}'

curl -X DELETE localhost:8000/api/orders/{orderId}  \
   -H 'Content-Type: application/json'  \
	 -H "Authorization: Bearer {token}" 
```

*Allowed status values are 0 and 1, for True and False respectively.*

### Purchase

**/api/purchases**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Customer | GET | Retrieve purchases list | Other users’ purchases are unreachable |
| Delivery Crew | GET | Retrieve purchases list | Can only retrieve purchases related to orders assign to them |
| Manager | GET | Retrieve purchases list | None |
| Admin | GET | Retrieve purchases list | None |

**Usage**:

```bash
curl -X GET localhost:8000/api/purchases \
   -H 'Content-Type: application/json'   \
	 -H "Authorization: Bearer {token}"
```

**/api/purchases/{purchaseId}**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Customer | GET | Retrieve the purchase | Other users’ purchases are unreachable |
| Delivery Crew | GET | Retrieve the purchase | Can only retrieve purchases related to orders assign to them |
| Manager | GET, DELETE | Retrieve and delete the purchase | None |
| Admin | GET, DELETE | Retrieve and delete the purchase | None |

**Usage**:

```bash
curl -X GET localhost:8000/api/purchases/{purchaseId} \
   -H 'Content-Type: application/json'  \
	 -H "Authorization: Bearer {token}"

curl -X DELETE localhost:8000/api/purchases/{purchaseId} \
   -H 'Content-Type: application/json'  \
	 -H "Authorization: Bearer {token}"  
```

### Purchase Items

**/api/purchase-items**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Customer | GET | Retrieve purchase-items lust | Other users’ purchase-items are unreachable |
| Delivery Crew | GET | Retrieve purchase-items lust | Can only retrieve purchase-items related to orders assign to them |
| Manager | GET | Retrieve purchase-items lust | None |
| Admin | GET | Retrieve purchase-items lust | None |

**Usage**:

```bash
curl -X GET localhost:8000/api/purchases/{purchaseId} \
   -H 'Content-Type: application/json'  \
	 -H "Authorization: Bearer {token}"

curl -X DELETE localhost:8000/api/purchases/{purchaseId} \
   -H 'Content-Type: application/json'  \
	 -H "Authorization: Bearer {token}"  
```

**/api/purchase-items/{purchase-itemId}**

| ROLE | ALLOWED METHODS | ACTIONS | RESTRICTIONS WITHIN ALLOWED METHODS |
| --- | --- | --- | --- |
| Customer | GET | Retrieve the purchase-item | Other users’ purchases are unreachable |
| Delivery Crew | GET | Retrieve the purchase-item | Can only retrieve purchases related to orders assign to them |
| Manager | GET, PATCH, DELETE | Retrieve, edit, and delete the purchase-item | None |
| Admin | GET, PATCH, DELETE | Retrieve, edit, and delete the purchase-item | None |

**Usage**:

```bash
curl -X GET localhost:8000/api/purchases/{purchaseId} \
   -H 'Content-Type: application/json'  \
	 -H "Authorization: Bearer {token}"

curl -X PATCH localhost:8000/api/purchases/{purchaseId} \
   -H 'Content-Type: application/json'  \
	 -H "Authorization: Bearer {token}"   \
   -d '{"quantity": "{value}"}'

curl -X DELETE localhost:8000/api/purchases/{purchaseId} \
   -H 'Content-Type: application/json'  \
	 -H "Authorization: Bearer {token}"  
```