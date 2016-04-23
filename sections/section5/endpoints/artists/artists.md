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

        Number of artists to show. The `count` value will be neglected if it is larger than the actual list count. If not specified, response will contain entire list. (Pagination feature will be added in near future)

      * `order`

        Order of artist shown based on `id` data of artist. `id` value represents the order of artist being added to the database. `desc` will show artist in descending order (From recent to older) whereas `asc` with show artist in ascending order (From older to recent). If not specified default `order` value is `asc`

* **Data Params:**
  `None`

* **Success Response:**

  ```
  {
    "meta" : {
      "response_code" : 200  
    },
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
  ```
  {
    "meta" : {
      "response_code" : 422 ,
      'error_type" : "UNPROCESSABLE ENTRY",
      "error_msg" : "order parameter invalid, try desc or asc",
    },
    "data" : null,
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
