# Django API 

##### Postman Requests collection link: 
[URL](https://go.postman.co/workspace/My-Workspace~60ee7954-5627-4d70-8dc5-c9e4b31d61ae/collection/13905733-02816b2d-92df-4248-ad82-d0e7e90dc174)


##### End point & json for adding advisor:

```https://django-proj-api.herokuapp.com/admin/advisor/```

```
{
    "name": "advisor 1",
    "profileUrl": "https://www.seekpng.com/png/detail/413-4139803_unknown-profile-profile-picture-unknown.png"
}
```

##### End point & json for Registering User:

```https://django-proj-api.herokuapp.com/user/register/```

```
{
    "name": "steven",
    "email": "steven@gmail.com",
    "password": "12345"
}
```

##### End point & json for Logging User:

```https://django-proj-api.herokuapp.com/user/register/```

```
{
    "email": "steven@gmail.com",
    "password": "12345"
}
```

##### End point and response of getting Advisors:

```https://django-proj-api.herokuapp.com/user/1/advisor```

```
[
    {
        "id": 1,
        "name": "advisor 1",
        "profileUrl": "https://www.seekpng.com/png/detail/413-4139803_unknown-profile-profile-picture-unknown.png"
    }
]
```

##### End point & json for booking call with an advisor:

```https://django-proj-api.herokuapp.com/user/1/advisor/1/```

```
{
    "bookingTime": "sunday, 31 oct 2021 02:04"
}
```

##### End point & response for getting booked calls:

```https://django-proj-api.herokuapp.com/user/1/advisor/booking```

```
{
    [
    {
        "advisor": "advisor 1",
        "advisorProfileUrl": "https://www.seekpng.com/png/detail/413-4139803_unknown-profile-profile-picture-unknown.png",
        "advisorId": 1,
        "bookingTime": "2021-10-31T11:32:18.959949Z",
        "id": 1
    }
]
}
```




