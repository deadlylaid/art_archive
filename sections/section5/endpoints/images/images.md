**images/**
----
  Returns json data for list of images

* **URL**

  /images

* **Method:**

  `GET`

*  **URL Params**

   * **Required:**
    `None`

   * **Optional:**

      * `count`

        Number of items to show. The `count` value will be neglected if it is larger than the actual list count. If not specified, response will contain entire list. (Pagination feature will be added in near future)

      * `order`

        Order of items shown based on `year` data of image, `desc` will show items in descending order whereas `asc` with show items in ascending order. If not specified default `order` value is `desc`
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
        "image_url": "https://image.path.jpg",
        "title": "Image title",
        "year": 2016,
        "artist_id": 1,
        "artist_name": "Artist name",
        "description": "Image description",
        "detail_href": "path/to/image/detail/info",
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
      url: "/images/?count=12&order=desc",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
