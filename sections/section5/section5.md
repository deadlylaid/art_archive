**ART_ARCHIVE API DOCUMENTATION**
----
* **Key Endpoints**
  * [Images](https://github.com/paulsoh/art_archive/blob/master/sections/section5/endpoint_images.md)
  * [Artists](https://github.com/paulsoh/art_archive/blob/master/sections/section5/endpoint_artists.md)

* **Response:**

    **Response** from ART_ARCHIVE REST API will be in the following structure

    * **In case of success:**

      * **Code:** 200 OK

        ```
        {
          "meta" : {
            "response_msg" : "verbose description about response (if necessary)"  
          },
          "data" : {
            "id" : 12,
          }
        }
        ```

    * **In case of error:**

      * **Code:** 422 UNPROCESSABLE ENTITY

        ```
        {
          "error" : "description about error",
        }
        ```

* **Notes:**
  This API Documentation is inspired(?) by:
    * https://gist.github.com/iros/3426278
