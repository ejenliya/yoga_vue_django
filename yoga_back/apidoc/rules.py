
"""
    @api {POST} /api/user/create-profile/ 1.1 Create user
    @apiName 1.1 Create user
    @apiGroup User
    @apiParam {String} first_name User first name
    @apiParam {String} last_name User last name
    @apiParam {String} image User avatar file

    @apiSuccess {String} status ok or error
    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "user_id": 1
    }
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 400
    {
        "non_field_errors": [
            "Unable to create user with provided credentials."
        ]
    }
"""

"""
    @api {GET} /api/user/profile/{user_id} 1.2 Get user profile
    @apiName 1.3 Get user
    @apiGroup User

    @apiParam {Number} user_id Users id
    @apiParam {String} first_name User first name
    @apiParam {String} last_name User last name
    @apiParam {String} image User avatar file

    @apiSuccess {Number} id User id
    @apiSuccess {String} first_name User first name
    @apiSuccess {String} last_name User last name
    @apiSuccess {String} image User avatar image

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "id": 1,
        "image": "http://api-yoga.maximusapp.com/media/YFDNcvTLEhqx.jpg",
        "first_name": "admin",
        "last_name": "admin"
    }
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 404 Not Found
"""


"""
    @api {PUT} /api/user/update-profile/{user_id} 1.4 Update user
    @apiName 1.4 Update user
    @apiGroup User
    
    @apiSuccess {Number} id User id
    @apiSuccess {String} first_name User first name
    @apiSuccess {String} last_name User last name
    @apiSuccess {String} image User avatar image


    @apiSuccess {Number} id User id
    @apiSuccess {String} first_name User first name
    @apiSuccess {String} last_name User last name
    @apiSuccess {String} image User avatar image

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "id": 1,
        "image": "http://api-yoga.maximusapp.com/media/YFDNcvTLEhqx.jpg",
        "first_name": "admin",
        "last_name": "admin"
    }
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 404 Not Found
"""

"""
    @api {GET} /api/workout/get-workout/{workout_id}/ 2.1 Get workout
    @apiName 2.1 Get wprkout
    @apiGroup Workout

    @apiParam {Number} workout_id Workout id


    @apiSuccess {Number} workout_id Workout id
    @apiSuccess {String} name workout name
    @apiSuccess {String} video Workout video file
    @apiSuccess {String} duration Workout duration  
    @apiSuccess {String} periodicity Workout periodicity
    @apiSuccess {String} level Простой средний продвинутый
    @apiSuccess {String} description workout description
    @apiSuccess {String} sex U M F
    @apiSuccess {String} value workout value
    @apiSuccess {String} image Workout image preview
    @apiSuccess {Object} troubles list of troubles objects


    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "workout_id": 4,
        "name": "t",
        "video": "http://api-yoga.maximusapp.com/Kitten_Zoom_Filter_Mishap_VEC0LdZ.mp4",
        "duration": "t",
        "periodicity": "4",
        "level": "Средний",
        "description": "t",
        "value": "t",
        "image": "http://api-yoga.maximusapp.com/kotik_LFuK6N5.jpg",
        "sex": "M",
        "troubles": [
            {
                "id": 3,
                "name":  "http://api-yoga.maximusapp.com/media/YFDNcvTLEhqx.jpg",
                "image":  "http://api-yoga.maximusapp.com/media/YF345TLEhqx.jpg"
            }
        ]
    }
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 404 Not Found

"""

"""
    @api {GET} /api/workout/get-workout-list/ 2.2 Workout List
    @apiName 2.2 Workout List
    @apiGroup Workout

    @apiSuccess {Object} list list of workout objects 

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        [
            {
                "id": 4,
                "name": "t",
                "video": "http://api-yoga.maximusapp.com/Kitten_Zoom_Filter_Mishap_VEC0LdZ.mp4",
                "duration": "t",
                "periodicity": "4",
                "level": "Средний",
                "image": "http://api-yoga.maximusapp.com/kotik_LFuK6N5.jpg",
                "description": "t",
                "value": "t",
                "sex": "M"
            }
        ]
    }
"""

"""
    @api {GET} /api/workout/get-workout-filtered-list/ 2.3 Workout filtered List
    @apiName 2.3 Workout filtered List
    @apiGroup Workout

    @apiParam {String} sex Workout sex
    @apiParam {String} peridoicity Workout peridoicity
    @apiParam {String} level Workout level
    @apiParam {Object} troubles Trouble objects id's list

    @apiSuccess {Number} id Reques id
    @apiSuccess {String} name workout name
    @apiSuccess {String} image workout image

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        [
            {
                "id": 4,
                "name": "t",
                "image": "http://api-yoga.maximusapp.com/kotik_LFuK6N5.jpg"
            }
        ]
    }
"""

"""
    @api {GET} /api/workout/get-trouble-list/ 3.1 Get trouble list
    @apiName 3.1 Get trouble list
    @apiGroup Trouble

    @apiSuccess {Number} id trouble id
    @apiSuccess {String} name trouble name
    @apiSuccess {String} image trouble image link

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        [
            {
                "id": 2,
                "name": "Тестовая пробема",
                "image": "http://api-yoga.maximusapp.com/test_6d69TZ3.jpg"
            },
            {
                "id": 3,
                "name": "Вторая тестовая проблема",
                "image": "http://api-yoga.maximusapp.com/ghrweherherh_dtDHOan.jpg"
            }
        ]
    }
"""