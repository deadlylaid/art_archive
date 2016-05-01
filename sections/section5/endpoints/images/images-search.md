**images/search**
----
  Returns json data for images retrieved by queried parameters(values)

* **URL**

  images/search/

* **Method:**

  `GET`

*  **URL Params**
  + At least *one* parameter is required for search function.
  + More than *one* parameter is supported for making queries.

   * **Required:**
    `None`

   * **Optional:**
      * `title`

        usage:
        `/images/search/?title=모나리자`

      * `year`

        usage:
        `/images/search/?year=1517&title=모나리자`

      * `artist_name`

        usage:
        `/images/search/?artist_name=레오나르도 다 빈치&year=1517&title=모나리자`

      * `genre`

        usage:
        `/images/search/?genre=르네상스&artist_name=레오나르도 다 빈치&year=1517&title=모나리자`

      * `description`

        usage:
        `/images/search/?description=나무판 위에 유채&genre=르네상스&artist_name=레오나르도 다 빈치&year=1517&title=모나리자`

      * `max_items`

        Number of images to show. If value of `max_item` if larger than actual items in query result, it will be stated in `response_msg` within `meta`
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

        Order of items shown based on `year` data of image, `desc` will show items in descending order whereas `asc` with show items in ascending order. If not specified default `order` value is `desc`

* **Data Params:**
  `None`


* **Success Response:**

  * **Code:** 200 OK

    ```
    {
      "data" : [
        {
          "id" : 12,
          "image_url": "https://image.path.jpg",
          "title": "모나리자",
          "year": 1517,
          "artist_id": 151,
          "artist_name": "레오나르도 다 빈치",
          "description": "나무판 위에 유채",
          "detail_href": "path/to/image/detail/info",
        },
        {
            ...,
        },
      ]
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
      "error" : "invalid parameter, supported parameters are title, year, artist_name, description, genre"
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
      url: "/images/search/?title=모나리자",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
