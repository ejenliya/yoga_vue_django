
"""
    @apiName 3 Get troubles list
    @apiGroup Trouble

    @api {get}/api/workout/get-trouble-list/  3 Get troubles list
    @apiSampleRequest http://apidoc.maximusapp.com

    @apiSuccess {int} workout_id ID
    @apiSuccess {str} name Name
    @apiSuccess {str} image Image
    
    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "results": [
            {
                "id": 2,
                "name": "котик вернулся на коленки",
                "image": "http://maximusapp.com/media/kotik_6d69TZ3.jpg"
            },
            {
                "id": 3,
                "name": "котик еще не на коленках",
                "image": "http://maximusapp.com/media/ghrweherherh_dtDHOan.jpg"
            }
        ]
    }
"""