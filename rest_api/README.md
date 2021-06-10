# Product Registry Service

## Usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all products

**Definition**

`GET /products`

**Response**

- `200 OK` on success

```json
[
    {
        "identifier": "prod1",
        "name": "Product 1",
        "product_type": "some-type",
    },
    {
        "identifier": "prod2",
        "name": "Product 2",
        "product_type": "some-other-type",
    },
]
```

### Registering a new product

**Definition**

`POST /products`

**Arguments**

- `"identifier":string` a globally unique identifier for this product
- `"name":string` a friendly name for this product
- `"product_type":string` the type of the product as understood by the client

If a product with the given identifier already exists, the existing product will be overwritten.

**Response**

- `201 Created` on success

```json
    {
        "identifier": "prod2",
        "name": "Product 2",
        "product_type": "some-other-type",
    }
```

## Lookup product details

`GET /product/<identifier>`

**Response**

- `404 Not Found` if the product does not exist
- `200 OK` on success

```json
    {
        "identifier": "prod2",
        "name": "Product 2",
        "product_type": "some-other-type",
    }
```

## Delete a product

**Definition**

`DELETE /product/<identifier>`
 
**Response**

- `404 Not Found` if the product does not exist
- `204 No Content` on success
