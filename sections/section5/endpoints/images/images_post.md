**images/**
----
  Add(insert) image data to database

* **URL**

  images/

* **Method:**

  `POST`

*  **URL Params**
  * **Required:**
  `None`
  * **Optional:**
  `None`


* **Data Params:**

    > **Important!** For the image to be successfully created, you must make sure that the `artist_name` already exists in our database. If not, image will not be created. To add new artists first, go [here](https://github.com/paulsoh/art_archive/blob/master/sections/section5/endpoints/artists/artists_post.md)

  * **Required:**
    To add new images to the database, you must have the following data parameters

    * `title`: `[String]` title of the image
    * `image_url`: `[String]` url of the image
    * `image_year`: `[Integer]` year when image was released
    * `artist_name`: `[String]` artist name of the image
    * `image_description`: `[String]` brief description of the image

  * **Optional:**
   `None`

* **Success Response:**

 * **Code:** 201 CREATED

   ```
   {
     "data" : {
       "id" : 12,
       "image_url": "https://new.image.path.jpg",
       "title": "New Image title",
       "year": 2016,
       "artist_id": 1,
       "artist_name": "Artist name",
       "description": "New Image description",
       "artist_href": "path/to/artist/info",
     }
   }
   ```

* **Error Response:**

 * **Code:** 422 UNPROCESSABLE ENTRY

   ```
   {
     "error" : "artist_name not found, artist_name should be in our artists database to add new image.",
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
      url: "/images/",
      dataType: "json",
      type : "POST",
      data : {
        "title": "Image title",
        "image_url": "Image URL",
        "image_year": 2016,
        "artist_name": "Artist Name",
        "image_description": "Image Description",
      }
      success : function(r) {
        console.log(r);
      }
    });
  ```
