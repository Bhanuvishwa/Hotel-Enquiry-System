# DBMS Project for Hotel Management System

Our project is about making a web-app with DB which makes people easier to find hotels and thereby making their stay facilities more comfortable with accurate information about hotels. Our Database helps people to view all hotels in the city including the details like price, area where the hotel is located, reviews, no. of rooms available, types of rooms available.

Pre-requisite: Xampp App.

1) Admin
•	Update manager details
•	Update hotel details
•	Update rooms
•	View manager details
•	View hotels

2) Manager
•	Update details of particular hotel
•	View hotel details
•	View rooms

3) Client
•	Login and Sign up
•	View hotels
•	View room details


### Admin:
 A) For updating manager details, 
FRONTEND Order: LOGIN.php --> admindisplay.html --> ha[hotelnumber].php
BACKEND Order: 1) auth.php checks login credentials of manager.
       2) If creds are valid, it directs to admindisplay.php.
       3) In admindisplay.php, we will be able to update room details.
       4) For selecting one of hotels, admin has to choose one hotel and it redirects to ha1.php [If he is selecting hotel 1].
Details will be taken in a form and ha1.php send the details into dupe1.php which will update the values in database.

B) For updating rooms, hotel details:
FRONTEND Order: LOGIN.php --> admindisplay.html --> ha[hotelnumber].php
BACKEND Order: 1) auth.php checks login credentials of manager.
       2) If creds are valid, it directs to admindisplay.php.
       3) In admindisplay.php, we will be able to update room details.
       4) For selecting one of hotels, admin has to choose one hotel and it redirects to ha1.php [If he is selecting hotel 1].
Details will be taken in a form and ha1.php send the details into x1.php which will update the values in database.

C) Viewing Hotel and Room Details:
FRONTEND Order: LOGIN.php --> admindisplay.html --> ha[hotel no.].php
Using ha1.php managers will see updated values from databases through respective SQL queries.

D) Viewing Manager Details:
FRONTEND Order: LOGIN.php --> admindisplay.html --> ha[hotel no.].php
Using ha1.php managers will see updated values from databases through respective SQL queries.
 
### MANAGER:
A) For updating hotel and room details, 
FRONTEND Order: LOGIN.php --> manager1.php
BACKEND Order: 1) auth.php checks login credentials of manager.
       2) If creds are valid, it directs to manager.php.
       3) In manager.php, manager will be able to update room details.
Details will be taken in a form and send the details into xyz.php which will update the values in database.

B) Viewing Hotel and Room Details:
FRONTEND Order: LOGIN.php --> hoteldisplay.html --> [hotelname].php
Using manager1.php managers will see updated values from databases. 
 
### END-USER:
A) Viewing Hotel Details:
   FRONTEND Order: LOGIN.php --> hoteldisplay.html --> [hotelname].php
   Using [hotel name]_details.php users will be able to see latest details from database.  
