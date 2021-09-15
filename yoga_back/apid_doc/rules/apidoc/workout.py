"""
    @apiName 2 Get workout
    @apiGroup Workout

    @api {get}/api/workout/get-workout/{workout_id}/ 2 Get workout
    @apiSampleRequest http://apidoc.maximusapp.com

    @apiParam {Number} workout_id Id-Workout.

    @apiSuccess {int} workout_id ID
    @apiSuccess {str} name Name
    @apiSuccess {str} video video
    @apiSuccess {int} duration duration
    @apiSuccess {str} periodicity Workout periodicity
    @apiSuccess {str} level Workout difficulty level
    @apiSuccess {str} description Description
    @apiSuccess {str} value value
    @apiSuccess {str} sex Sex
    @apiSuccess {str} image Image
    @apiSuccess {objects} troubles Troubles

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "workout_id": 4,
        "name": "t",
        "video": "http://maximusapp.com/media/Kitten_Zoom_Filter_Mishap_VEC0LdZ.mp4",
        "duration": "t",
        "periodicity": "4",
        "level": "Средний",
        "description": "t",
        "value": "t",
        "image": "http://maximusapp.com/media/kotik_LFuK6N5.jpg",
        "sex": "M",
        "troubles": [
            {
                "id": 3,
                "name": "котик еще не на коленках",
                "image": "http://maximusapp.com/media/Без_названия_dtDHOan.jpg"
            }
        ]
    }
"""

"""
    @apiName 2.1 Get workout filtered list
    @apiGroup Workout

    @api {get}/api/workout/get-workout-filtered-list/ 2.1 Get workout filtered list
    @apiSampleRequest http://apidoc.maximusapp.com

    @apiParam {String} Sex
    @apiParam {Number} Peridoicity
    @apiParam {String} Level
    @apiParam {Objects} Trouble id's array

    @apiSuccess {int} workout_id ID
    @apiSuccess {str} name Name
    @apiSuccess {str} image Image
    
    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
      "results": [
            {
                "id": 4,
                "name": "t",
                "image": "http://maximusapp.com/media/kotik_LFuK6N5.jpg"
            }
        ]
    }
"""