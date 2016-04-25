**artists/`artist-id`/artworks/**
----
  Returns json data for artworks by artist with id:`artist-id`

* **URL**

  artists/`artist-id`/artworks/

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
    + The structure of the success response is identical to the success response of `images/`.

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
    ],
  }
  ```

* **Error Response:**
  ```
  {
    "meta" : {
      "response_code" : 404 ,
      'error_type" : "NOT FOUND",
      "error_msg" : "URL path invalid, check artist_id",
    },
    "data" : null,
  }
  ```
  
  ```
  {
    "meta" : {
      "response_code" : 500 ,
      'error_type" : "INTERNAL SERVER ERROR",
      "error_msg" : "The server encountered an unexpected condition which prevented it
   from fulfilling the request.",
    },
    "data" : null,
  }
  ```

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/artists/1/artworks/",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
