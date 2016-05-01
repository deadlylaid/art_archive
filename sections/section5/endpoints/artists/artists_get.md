**artists/**
----
  Returns json data for list of artists

* **URL**

  artists/

* **Method:**

  `GET`

*  **URL Params**

   * **Required:**
    `None`

   * **Optional:**

      * `count`

        Number of artists to show. The `count` value will be neglected if it is larger than the actual list count. If not specified, response will contain entire list.

      * `order`

        Order of artist shown based on `created_at` data of artist. `desc` will show artist in descending order, whereas `asc` with show artist in ascending order. If not specified default `order` value is `asc`


* **Data Params:**
  `None`

* **Success Response:**

  * **Code:** 200 OK

    ```
    {
      "data" : [
        {
          "id" : 12,
          "name": "Artist name",
          "birth_year": 1920,
          "death_year": 2000,
          "country": "미국",
          "genre": "인상주의",
          "detail_href": "path/to/artist/detail/info",
        },
        {
            ...,
        },
      ]
    }
    ```

* **Error Response:**

  * **Code:** 422 UNPROCESSABLE ENTRY

    ```
    {
      "error" : "order parameter invalid, try desc or asc",
    }
    ```

  * **Code:** 500 INTERNAL SERVER ERROR

    ```
    {
      "error" : "The server encountered an unexpected condition which prevented it from fulfilling the request.",
    }
    ```

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/artists/",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
