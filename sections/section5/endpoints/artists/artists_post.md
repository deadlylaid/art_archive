**artists/**
----
  Add(insert) an artist to database

* **URL**

  artists/

* **Method:**

  `POST`

*  **URL Params**
  * **Required:**
  `None`
  * **Optional:**
  `None`


* **Data Params:**

  * **Required:**
    To add new artist to the database, you must have the following data parameters

    * `name`: `[String]` name of the artist
    * `country`: `[String]` nationality of the artist
    * `genre`: `[String]` genre of the artist's artwork

  * **Optional:**

    > If not specified, optional parameters will be set as `null`

    * `birth_year`: `[Integer]` year of birth of artist
    * `death_year`: `[Integer]` year of death of artist


* **Success Response:**

  * **Code:** 201 CREATED

    ```
    {
      "data" : {
        "id" : 12,
        "name": "New Artist name",
        "birth_year": null,
        "death_year": null,
        "country": "미국",
        "genre": "인상주의",
        "artworks_href": "path/to/artworks/for/artist",
      },
    }
    ```

* **Error Response:**

  * **Code:** 422 UNPROCESSABLE ENTRY

    ```
    {
      "error" : "name field is required for adding an artist.",
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
      url: "/artists/",
      dataType: "json",
      type : "POST",
      data : {
        "name": "Artist name",
        "country": "미국",
        "genre": "초 현실주의",
        "birth_year": 1990,
      }
      success : function(r) {
        console.log(r);
      }
    });
  ```
