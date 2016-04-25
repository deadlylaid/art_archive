**ART_ARCHIVE API DOCUMENTATION**
----
* **Key Endpoints**
  * [Images](https://github.com/paulsoh/art_archive/blob/master/sections/section5/endpoint_images.md)
  * [Artists](https://github.com/paulsoh/art_archive/blob/master/sections/section5/endpoint_artists.md)

* **Response:**

    Any kind of **Response** from ART_ARCHIVE REST API will be in the following structure

    ```
    {
      "meta" : {
        "response_code" : 200,
      },
      "data" : ...
    }
    ```

    * **In case of success:**
    ```
    {
      "meta" : {
        "response_code" : 200  
      },
      "data" : {
        "id" : 12,
      }
    }
    ```
    * **In case of error:**
    ```
    {
      "meta" : {
        "response_code" : 422 ,
        'error_type" : "UNPROCESSABLE ENTRY",
        "error_msg" : "Email invalid",
      },
      "data" : null,
    }
    ```

    ```
    {
      "meta" : {
        "response_code" : 401 ,
        'error_type" : "UNAUTHORIZED",
        "error_msg" : "Log in",
      },
      "data" : null,
    }
    ```

* **Notes:**
  This API Documentation is inspired(?) by:
    * https://gist.github.com/iros/3426278
