**artists/`artist-id`**
----
  Returns json data for artist with id:`artist-id`

* **URL**

  artists/`artist-id`/

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
        "name": "Artist name",
        "birth_year": 1920,
        "death_year": 2000,
        "country": "미국",
        "genre": "인상주의",
        "artworks_href": "path/to/artworks/for/artist",
      },
    }
    ```

* **Error Response:**

  * **Code:** 404 NOT FOUND

    ```
    {
      "error" : "URL path invalid, check artist_id",
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
      url: "/artists/1",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
