**images/`image-id`**
----
  Returns json data for image with id:`image-id`

* **URL**

  /images/`image-id`

* **Method:**

  `GET`

*  **URL Params**

   * **Required:**
    `None`

   * **Optional:**
    `None`

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
        "artist_href": "path/to/artist/info",
      }
    ]
  }
  ```

* **Error Response:**
  ```
  {
    "meta" : {
      "response_code" : 404 ,
      'error_type" : "NOT FOUND",
      "error_msg" : "URL path invalid, check image_id",
    },
    "data" : null,
  }
  ```

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/images/1",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
