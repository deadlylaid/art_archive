**images/`image-id`**
----
  Returns json data for image with id:`image-id`

* **URL**

  images/`image-id`/

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

  * **Code:** 200 OK

    ```
    {
      "data" : {
        "id" : 12,
        "image_url": "https://image.path.jpg",
        "title": "Image title",
        "year": 2016,
        "artist_id": 1,
        "artist_name": "Artist name",
        "description": "Image description",
        "artist_href": "path/to/artist/info",
      }
    }
    ```

* **Error Response:**

  * **Code:** 404 NOT FOUND

    ```
    {
      "error" : "URL path invalid, check image_id",
    }
    ```

  * **Code:** 500 INTERNAL SERVER ERROR

    ```
    {
      "error" : "The server encountered an unexpected condition which prevented it from fulfilling the request."
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
