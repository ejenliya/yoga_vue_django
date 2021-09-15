"""
    @apiName 1. GetUserProfile
    @apiGroup User

    @api {get}/api/user/profile/{user_id} 1. GetUserProfile
    @apiSampleRequest http://apidoc.maximusapp.com

    @apiParam {Number} user_id Id-User.

    @apiSuccess {int} user_id ID
    @apiSuccess {str} first_name First user name
    @apiSuccess {str} last_name Last user name
    @apiSuccess {str} image Image


    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "id": 1,
        "image": "http://maximusapp.com/media/YFDNcvTLEhqx.jpg",
        "first_name": "admin",
        "last_name": "admin"
    }
"""



"""
    @apiName 1.1 CreateUserProfile
    @apiGroup User

    @api {get}/api/user/create-profile/ 1.1 CreateUserProfile
    @apiSampleRequest http://apidoc.maximusapp.com

    @apiParam {str} first_name First user name
    @apiParam {str} last_name Last user name
    @apiParam {file} image Image ( send image file )

    @apiSuccess {int} user_id ID


    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "user_id": 1
    }
"""

"""
    @apiName 1.2 UpdateUserProfile
    @apiGroup User

    @api {get}/api/user/update-profile/{user_id} 1.2 UpdateUserProfile
    @apiSampleRequest http://apidoc.maximusapp.com

    @apiParam {Number} user_id Id-User.

    @apiParam {str} first_name First user name
    @apiParam {str} last_name Last user name
    @apiParam {str} image Image ( send image file )

    @apiSuccess {int} user_id ID
    @apiSuccess {str} first_name First user name
    @apiSuccess {str} last_name Last user name
    @apiSuccess {str} image Image


    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "user_id": 1,
        "image": "http://maximusapp.com/media/YFDNcvTLEhqx.jpg",
        "first_name": "admin",
        "last_name": "admin"
    }
"""