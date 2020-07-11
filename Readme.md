# Website Test

## Task 1 - (1 min of task) [2 points]
```
Clone this repository in your local system
```
```
Create app name "home" in this project
```
```
Create urls.py in home app and link in websitetest/urls.py
Eg.  path('',  include("home.urls")),
```

## Task 2 - (5 min of task) [5 points]
```
in models.py
from django.contrib import auth
```
```
Create model with name User with following information
  user - models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
  name - Char Field with max_length=20
  age - Integer Field with max_length=3, min_lengh=2 
```

## Task 3 - (5 min of task) [5 points]
```
Create url / and return page
return simple json data
Eg. { 
      name: 'Ava',
      age: 21
    }
help Note: return HttpResponse(..., content_type='application/json')
```

## Task 4 - (18 min of task) [15 points + 5 points + 5 points]
```
Create url /home/ and return page index.html as below content
```
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <!-- <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"> -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <title>Ava</title>
</head>

<body>Your page data will go here</body>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
</html>
```
```
Make home page to looks like an image home.jpg
```

Note: 
* Use bootstrap and minimize css as possible - No CSS will get you an extra points [5 points]
* Responsiveness will give you more extra points [5 points]

## Task 5 - (1 min of task) [3 points]
```
Create PR on github and submit your project
Notify us with PR link
```

## Total Time : 30 min [40 points] (But you have 3 days) :)

# bESt Of LucK
### Based on your performance you will get an opportunity to do work with us

