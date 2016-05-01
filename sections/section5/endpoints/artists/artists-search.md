**artists/search**
----
  Returns json data for artists retrieved by queried parameters(values)

* **URL**

  artists/search/

* **Method:**

  `GET`

*  **URL Params**
  + At least *one* parameter is required for search function.
  + More than *one* parameter is supported for making queries.

   * **Required:**
    `None`

   * **Optional:**
      * `name`

        usage:
        `/artists/search/?name=빈센트`

      * `country`

        usage:
        `/artists/search/?country=네더랜드&name=빈센트`

      * `genre`

        usage:
        `/artists/search/?genre=인상주의&country=네더랜드&name=빈센트`

      * `alive_in`

        usage:
        `/artists/search/?alive_in=1877&genre=인상주의&country=네더랜드&name=빈센트`

      * `max_items`

        Number of artists to show. If value of `max_item` if larger than actual items in query result, it will be stated in `response_msg` within `meta`
        ```
        {
          "meta" : {
            "response_msg" : "requested with max_items: 20 but only 14 items were found matching the query",
          },
          "data" : [{

           },
           ...
           ]
        }
        ```
        If not specified, response will contain entire list. (Pagination feature will be added in near future)

      * `order`

        Order of artist shown based on `created_at` data of artist. `created_at` value represents the timestamp of when the artist was added to the database. `desc` will show artist in descending order (From most recent to least recent) whereas `asc` with show artist in ascending order (From least recent to most recent). If not specified default `order` value is `asc`

* **Data Params:**
  `None`

* **Success Response:**

  The structure of the success response is identical to the success response of `artists/`.

  * **Code:** 200 OK

    ```
    {
      "data" : [
        {
          "id" : 12,
          "created_at" : 1461570127,
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
      ],
    }
    ```

    + If no item is retrieved, response will be as following:

      ```
      {
          "meta" : {
            "response_msg" : "No results were retrieved from database",
          },
          "data" : null
      }
      ```

* **Error Response:**

  * **Code:** 422 UNPROCESSABLE ENTRY

    ```
    {
      "error" : "order parameter invalid, try desc or asc"
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
      url: "/artists/search/?alive_in=1877&genre=인상주의&country=네더랜드&name=빈센트",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
