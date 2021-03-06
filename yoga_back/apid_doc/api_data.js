define({ "api": [
  {
<<<<<<< HEAD
    "name": "3_Get_troubles_list",
    "group": "Trouble",
    "type": "get",
    "url": "/api/workout/get-trouble-list/",
    "title": "3 Get troubles list",
    "sampleRequest": [
      {
        "url": "http://api-yoga.maximusapp.com"
      }
    ],
=======
    "type": "GET",
    "url": "/api/workout/get-trouble-list/",
    "title": "3.1 Get trouble list",
    "name": "3.1_Get_trouble_list",
    "group": "Trouble",
>>>>>>> d23c3407b89679c29a8a44b2d470490263ae3583
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
<<<<<<< HEAD
            "type": "int",
            "optional": false,
            "field": "workout_id",
            "description": "<p>ID</p>"
          },
          {
            "group": "Success 200",
            "type": "str",
            "optional": false,
            "field": "name",
            "description": "<p>Name</p>"
          },
          {
            "group": "Success 200",
            "type": "str",
            "optional": false,
            "field": "image",
            "description": "<p>Image</p>"
=======
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>trouble id</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>trouble name</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "image",
            "description": "<p>trouble image link</p>"
>>>>>>> d23c3407b89679c29a8a44b2d470490263ae3583
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
<<<<<<< HEAD
          "content": "HTTP/1.1 200 OK\n{\n    \"results\": [\n        {\n            \"id\": 2,\n            \"name\": \"котик вернулся на коленки\",\n            \"image\": \"http://api-yoga.maximusapp.com/media/kotik_6d69TZ3.jpg\"\n        },\n        {\n            \"id\": 3,\n            \"name\": \"котик еще не на коленках\",\n            \"image\": \"http://api-yoga.maximusapp.com/media/ghrweherherh_dtDHOan.jpg\"\n        }\n    ]\n}",
=======
          "content": "HTTP/1.1 200 OK\n{\n    [\n        {\n            \"id\": 2,\n            \"name\": \"Тестовая пробема\",\n            \"image\": \"http://api-yoga.maximusapp.com/test_6d69TZ3.jpg\"\n        },\n        {\n            \"id\": 3,\n            \"name\": \"Вторая тестовая проблема\",\n            \"image\": \"http://api-yoga.maximusapp.com/ghrweherherh_dtDHOan.jpg\"\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 without token\n{\n    \"status\": \"invalid token\"\n}",
>>>>>>> d23c3407b89679c29a8a44b2d470490263ae3583
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
<<<<<<< HEAD
    "filename": "apidoc/trouble.py",
    "groupTitle": "Trouble"
  },
  {
    "name": "1.1_CreateUserProfile",
    "group": "User",
    "type": "get",
    "url": "/api/user/create-profile/",
    "title": "1.1 CreateUserProfile",
    "sampleRequest": [
      {
        "url": "http://api-yoga.maximusapp.com"
      }
    ],
=======
    "filename": "apidoc/rules.py",
    "groupTitle": "Trouble"
  },
  {
    "type": "POST",
    "url": "/api/user/create-profile/",
    "title": "1.1 Create user",
    "name": "1.1_Create_user",
    "group": "User",
>>>>>>> d23c3407b89679c29a8a44b2d470490263ae3583
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
<<<<<<< HEAD
            "type": "str",
            "optional": false,
            "field": "first_name",
            "description": "<p>First user name</p>"
          },
          {
            "group": "Parameter",
            "type": "str",
            "optional": false,
            "field": "last_name",
            "description": "<p>Last user name</p>"
          },
          {
            "group": "Parameter",
            "type": "file",
            "optional": false,
            "field": "image",
            "description": "<p>Image ( send image file )</p>"
=======
            "type": "String",
            "optional": false,
            "field": "first_name",
            "description": "<p>User first name</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "last_name",
            "description": "<p>User last name</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "image",
            "description": "<p>User avatar file</p>"
>>>>>>> d23c3407b89679c29a8a44b2d470490263ae3583
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
<<<<<<< HEAD
            "type": "int",
            "optional": false,
            "field": "user_id",
            "description": "<p>ID</p>"
=======
            "type": "String",
            "optional": false,
            "field": "status",
            "description": "<p>ok or error</p>"
>>>>>>> d23c3407b89679c29a8a44b2d470490263ae3583
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"user_id\": 1\n}",
          "type": "json"
        }
      ]
    },
<<<<<<< HEAD
    "version": "0.0.0",
    "filename": "apidoc/user.py",
    "groupTitle": "User"
  },
  {
    "name": "1.2_UpdateUserProfile",
    "group": "User",
    "type": "get",
    "url": "/api/user/update-profile/{user_id}",
    "title": "1.2 UpdateUserProfile",
    "sampleRequest": [
      {
        "url": "http://api-yoga.maximusapp.com"
      }
    ],
=======
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 400\n{\n    \"non_field_errors\": [\n        \"Unable to create user with provided credentials.\"\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "User"
  },
  {
    "type": "GET",
    "url": "/api/user/profile/{user_id}",
    "title": "1.2 Get user profile",
    "name": "1.3_Get_user",
    "group": "User",
>>>>>>> d23c3407b89679c29a8a44b2d470490263ae3583
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "user_id",
<<<<<<< HEAD
            "description": "<p>Id-User.</p>"
          },
          {
            "group": "Parameter",
            "type": "str",
            "optional": false,
            "field": "first_name",
            "description": "<p>First user name</p>"
          },
          {
            "group": "Parameter",
            "type": "str",
            "optional": false,
            "field": "last_name",
            "description": "<p>Last user name</p>"
          },
          {
            "group": "Parameter",
            "type": "str",
            "optional": false,
            "field": "image",
            "description": "<p>Image ( send image file )</p>"
=======
            "description": "<p>Users id</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "first_name",
            "description": "<p>User first name</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "last_name",
            "description": "<p>User last name</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "image",
            "description": "<p>User avatar file</p>"
>>>>>>> d23c3407b89679c29a8a44b2d470490263ae3583
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
<<<<<<< HEAD
            "type": "int",
            "optional": false,
            "field": "user_id",
            "description": "<p>ID</p>"
          },
          {
            "group": "Success 200",
            "type": "str",
            "optional": false,
            "field": "first_name",
            "description": "<p>First user name</p>"
          },
          {
            "group": "Success 200",
            "type": "str",
            "optional": false,
            "field": "last_name",
            "description": "<p>Last user name</p>"
          },
          {
            "group": "Success 200",
            "type": "str",
            "optional": false,
            "field": "image",
            "description": "<p>Image</p>"
=======
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>User id</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "first_name",
            "description": "<p>User first name</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "last_name",
            "description": "<p>User last name</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "image",
            "description": "<p>User avatar image</p>"
>>>>>>> d23c3407b89679c29a8a44b2d470490263ae3583
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
<<<<<<< HEAD
          "content": "HTTP/1.1 200 OK\n{\n    \"user_id\": 1,\n    \"image\": \"http://api-yoga.maximusapp.com/media/YFDNcvTLEhqx.jpg\",\n    \"first_name\": \"admin\",\n    \"last_name\": \"admin\"\n}",
=======
          "content": "HTTP/1.1 200 OK\n{\n    \"id\": 1,\n    \"image\": \"http://api-yoga.maximusapp.com/media/YFDNcvTLEhqx.jpg\",\n    \"first_name\": \"admin\",\n    \"last_name\": \"admin\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 404 Not Found",
>>>>>>> d23c3407b89679c29a8a44b2d470490263ae3583
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
<<<<<<< HEAD
    "filename": "apidoc/user.py",
    "groupTitle": "User"
  },
  {
    "name": "1._GetUserProfile",
    "group": "User",
    "type": "get",
    "url": "/api/user/profile/{user_id}",
    "title": "1. GetUserProfile",
    "sampleRequest": [
      {
        "url": "http://api-yoga.maximusapp.com"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "user_id",
            "description": "<p>Id-User.</p>"
          }
        ]
      }
    },
=======
    "filename": "apidoc/rules.py",
    "groupTitle": "User"
  },
  {
    "type": "PUT",
    "url": "/api/user/update-profile/{user_id}",
    "title": "1.4 Update user",
    "name": "1.4_Update_user",
    "group": "User",
>>>>>>> d23c3407b89679c29a8a44b2d470490263ae3583
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
<<<<<<< HEAD
            "type": "int",
            "optional": false,
            "field": "user_id",
            "description": "<p>ID</p>"
          },
          {
            "group": "Success 200",
            "type": "str",
            "optional": false,
            "field": "first_name",
            "description": "<p>First user name</p>"
          },
          {
            "group": "Success 200",
            "type": "str",
            "optional": false,
            "field": "last_name",
            "description": "<p>Last user name</p>"
          },
          {
            "group": "Success 200",
            "type": "str",
            "optional": false,
            "field": "image",
            "description": "<p>Image</p>"
=======
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>User id</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "first_name",
            "description": "<p>User first name</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "last_name",
            "description": "<p>User last name</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "image",
            "description": "<p>User avatar image</p>"
>>>>>>> d23c3407b89679c29a8a44b2d470490263ae3583
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"id\": 1,\n    \"image\": \"http://api-yoga.maximusapp.com/media/YFDNcvTLEhqx.jpg\",\n    \"first_name\": \"admin\",\n    \"last_name\": \"admin\"\n}",
          "type": "json"
        }
      ]
    },
<<<<<<< HEAD
    "version": "0.0.0",
    "filename": "apidoc/user.py",
    "groupTitle": "User"
  },
  {
    "name": "2.1_Get_workout_filtered_list",
    "group": "Workout",
    "type": "get",
    "url": "/api/workout/get-workout-filtered-list/",
    "title": "2.1 Get workout filtered list",
    "sampleRequest": [
      {
        "url": "http://api-yoga.maximusapp.com"
      }
    ],
=======
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 404 Not Found",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "User"
  },
  {
    "type": "GET",
    "url": "/api/workout/get-workout/{workout_id}/",
    "title": "2.1 Get workout",
    "name": "2.1_Get_wprkout",
    "group": "Workout",
>>>>>>> d23c3407b89679c29a8a44b2d470490263ae3583
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
<<<<<<< HEAD
            "type": "String",
            "optional": false,
            "field": "Sex",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "Peridoicity",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "Level",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Objects",
            "optional": false,
            "field": "Trouble",
            "description": "<p>id's array</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "int",
            "optional": false,
            "field": "workout_id",
            "description": "<p>ID</p>"
          },
          {
            "group": "Success 200",
            "type": "str",
            "optional": false,
            "field": "name",
            "description": "<p>Name</p>"
          },
          {
            "group": "Success 200",
            "type": "str",
            "optional": false,
            "field": "image",
            "description": "<p>Image</p>"
=======
            "type": "Number",
            "optional": false,
            "field": "workout_id",
            "description": "<p>Workout id</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "workout_id",
            "description": "<p>Workout id</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>workout name</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "video",
            "description": "<p>Workout video file</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "duration",
            "description": "<p>Workout duration</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "periodicity",
            "description": "<p>Workout periodicity</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "level",
            "description": "<p>Простой средний продвинутый</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "description",
            "description": "<p>workout description</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "sex",
            "description": "<p>U M F</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "value",
            "description": "<p>workout value</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "image",
            "description": "<p>Workout image preview</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "troubles",
            "description": "<p>list of troubles objects</p>"
>>>>>>> d23c3407b89679c29a8a44b2d470490263ae3583
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
<<<<<<< HEAD
          "content": "HTTP/1.1 200 OK\n{\n  \"results\": [\n        {\n            \"id\": 4,\n            \"name\": \"t\",\n            \"image\": \"http://api-yoga.maximusapp.com/media/kotik_LFuK6N5.jpg\"\n        }\n    ]\n}",
=======
          "content": "HTTP/1.1 200 OK\n{\n    \"workout_id\": 4,\n    \"name\": \"t\",\n    \"video\": \"http://api-yoga.maximusapp.com/Kitten_Zoom_Filter_Mishap_VEC0LdZ.mp4\",\n    \"duration\": \"t\",\n    \"periodicity\": \"4\",\n    \"level\": \"Средний\",\n    \"description\": \"t\",\n    \"value\": \"t\",\n    \"image\": \"http://api-yoga.maximusapp.com/kotik_LFuK6N5.jpg\",\n    \"sex\": \"M\",\n    \"troubles\": [\n        {\n            \"id\": 3,\n            \"name\":  \"http://api-yoga.maximusapp.com/media/YFDNcvTLEhqx.jpg\",\n            \"image\":  \"http://api-yoga.maximusapp.com/media/YF345TLEhqx.jpg\"\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 404 Not Found",
>>>>>>> d23c3407b89679c29a8a44b2d470490263ae3583
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
<<<<<<< HEAD
    "filename": "apidoc/workout.py",
    "groupTitle": "Workout"
  },
  {
    "name": "2_Get_workout",
    "group": "Workout",
    "type": "get",
    "url": "/api/workout/get-workout/{workout_id}/",
    "title": "2 Get workout",
    "sampleRequest": [
      {
        "url": "http://apidoc.maximusapp.com"
      }
    ],
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "workout_id",
            "description": "<p>Id-Workout.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "int",
            "optional": false,
            "field": "workout_id",
            "description": "<p>ID</p>"
          },
          {
            "group": "Success 200",
            "type": "str",
            "optional": false,
            "field": "name",
            "description": "<p>Name</p>"
          },
          {
            "group": "Success 200",
            "type": "str",
            "optional": false,
            "field": "video",
            "description": "<p>video</p>"
          },
          {
            "group": "Success 200",
            "type": "int",
            "optional": false,
            "field": "duration",
            "description": "<p>duration</p>"
          },
          {
            "group": "Success 200",
            "type": "str",
            "optional": false,
            "field": "periodicity",
            "description": "<p>Workout periodicity</p>"
          },
          {
            "group": "Success 200",
            "type": "str",
            "optional": false,
            "field": "level",
            "description": "<p>Workout difficulty level</p>"
          },
          {
            "group": "Success 200",
            "type": "str",
            "optional": false,
            "field": "description",
            "description": "<p>Description</p>"
          },
          {
            "group": "Success 200",
            "type": "str",
            "optional": false,
            "field": "value",
            "description": "<p>value</p>"
          },
          {
            "group": "Success 200",
            "type": "str",
            "optional": false,
            "field": "sex",
            "description": "<p>Sex</p>"
          },
          {
            "group": "Success 200",
            "type": "str",
            "optional": false,
            "field": "image",
            "description": "<p>Image</p>"
          },
          {
            "group": "Success 200",
            "type": "objects",
            "optional": false,
            "field": "troubles",
            "description": "<p>Troubles</p>"
=======
    "filename": "apidoc/rules.py",
    "groupTitle": "Workout"
  },
  {
    "type": "GET",
    "url": "/api/workout/get-workout-list/",
    "title": "2.2 Workout List",
    "name": "2.2_Workout_List",
    "group": "Workout",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "list",
            "description": "<p>list of workout objects</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    [\n        {\n            \"id\": 4,\n            \"name\": \"t\",\n            \"video\": \"http://api-yoga.maximusapp.com/Kitten_Zoom_Filter_Mishap_VEC0LdZ.mp4\",\n            \"duration\": \"t\",\n            \"periodicity\": \"4\",\n            \"level\": \"Средний\",\n            \"image\": \"http://api-yoga.maximusapp.com/kotik_LFuK6N5.jpg\",\n            \"description\": \"t\",\n            \"value\": \"t\",\n            \"sex\": \"M\"\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 without token\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Workout"
  },
  {
    "type": "GET",
    "url": "/api/workout/get-workout-filtered-list/",
    "title": "2.3 Workout filtered List",
    "name": "2.3_Workout_filtered_List",
    "group": "Workout",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "sex",
            "description": "<p>Workout sex</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "peridoicity",
            "description": "<p>Workout peridoicity</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "level",
            "description": "<p>Workout level</p>"
          },
          {
            "group": "Parameter",
            "type": "Object",
            "optional": false,
            "field": "troubles",
            "description": "<p>Trouble objects id's list</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Reques id</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>workout name</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "image",
            "description": "<p>workout image</p>"
>>>>>>> d23c3407b89679c29a8a44b2d470490263ae3583
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
<<<<<<< HEAD
          "content": "HTTP/1.1 200 OK\n{\n    \"workout_id\": 4,\n    \"name\": \"t\",\n    \"video\": \"http://maximusapp.com/media/Kitten_Zoom_Filter_Mishap_VEC0LdZ.mp4\",\n    \"duration\": \"t\",\n    \"periodicity\": \"4\",\n    \"level\": \"Средний\",\n    \"description\": \"t\",\n    \"value\": \"t\",\n    \"image\": \"http://maximusapp.com/media/kotik_LFuK6N5.jpg\",\n    \"sex\": \"M\",\n    \"troubles\": [\n        {\n            \"id\": 3,\n            \"name\": \"котик еще не на коленках\",\n            \"image\": \"http://maximusapp.com/media/Без_названия_dtDHOan.jpg\"\n        }\n    ]\n}",
=======
          "content": "HTTP/1.1 200 OK\n{\n    [\n        {\n            \"id\": 4,\n            \"name\": \"t\",\n            \"image\": \"http://api-yoga.maximusapp.com/kotik_LFuK6N5.jpg\"\n        }\n    ]\n}",
>>>>>>> d23c3407b89679c29a8a44b2d470490263ae3583
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
<<<<<<< HEAD
    "filename": "apidoc/workout.py",
=======
    "filename": "apidoc/rules.py",
>>>>>>> d23c3407b89679c29a8a44b2d470490263ae3583
    "groupTitle": "Workout"
  }
] });
