**images/**
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

  ```
  {
    "meta" : {
      "response_code" : 201  
    },
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
  ```
  {
    "meta" : {
      "response_code" : 422 ,
      'error_type" : "UNPROCESSABLE ENTRY",
      "error_msg" : "name field is required for adding an artist.",
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
      url: "/images/",
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
