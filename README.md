# Note: Unfortunately and frustratingly, This Project is not yet finished. I will admit that Django has been a difficult and lengthy subject to fully get to grips with, and although progress has been made, it has been a slow learning curve. Throughout creation and deployment of this project I seemed to encounter an extensive list of issues, most notably and time consuming has been trying to solve issues with my booking form data not reaching the backend server and therefor not being able to display it on the front end. Only bookings made via the admin panel had CRUD functionality. But with determination it is my goal to have this project fully finished and at something of a decent standard.

# The Pizza Project

Welcome to The Pizza Project. Our aim is to provide the local and surrounding communities of Bristol with the freshest and highest quality pizza imaginable, outside of Italy or the pizza hotspots of the USA. We craft out pizza sauce and dough every morning, then load up our mobile pizza truck and head out on the open road where we top and cook our pizzas to order on site. Wether that is at your front door, wedding venue, high street or charity event. If we can drive there, we can cook there. Our pizzas are cooked in a wood fired pizza oven in the back of our pizza truck to ensure that authentic pizza experience.
 
The live link to The Pizza Project website can be found here: *website link here*

- *Home page screen shot here*

This project, based on a fictitous mobile pizza restaurant of my own deisgn but inspired by a company with a similar business model from the local area of my home town in Bristol. Is designed to allow customers to create and log into an account, and to book The Pizza Project mobile truck on a selected date, and have the option to leave a comment on their booking. As well as for the business owner to log into the website as the super user, to manage their bookings and menu.

## Contents

The Contents of this site include,

- A base html template, that handles the navbar and footer across all pages. Allowing for the ability to write once and reuse across the site by using block tags.

- The Home page, featuring our masthead image and brand name, with a short introduction to The Pizza Project. It was originally intended to host the booking form also, but this was eventually moved to the profiles page.

- The Menu page features a custom WePik image used for the menu itself. Designed to be straight to the point, but with scope to possibly improve upon this page in a future release by adding menu items, prices and nutritional information into a database and then displayed to allow for better customisation by the site owner.

- Enquiries is a basic page found on most sites with similar buisness models. Featuring some images and brief snippets of text expanding some of what The Pizza Project can offer their customers, not mentioned in the Home page.

- Profile page, is intended for the Business Owner to view the collective of all the bookings made.

- User Bookings was intended to allow logged in users to make a booking, show those booking/s and also edit and delete them if required.

- Reigster, a page that allows users to register an account for The Pizza Project.

- Log In, a page that sits along side Register in the navbar that allows users to log in.

- Log Out, This page allows users to log out. It is hidden on the navbar to those that have yet to register/log in to The Pizza Project Website, then once signed in replaces the Register and Log In spots within the navbar.


## User Experience

### Strategy Plane

The primary site goal of The Pizza Project, was to server as a buisiness to consumer website for a fictious mobile food truck that specialised in New York Style pizza slices. Through a combination of displaying images of similar mobile pizza trucks, a menu and a booking form that could be submitted by users following registering/logging into the website, where they could also edit and delete their booking providing the were still logged in.

### Scope Plane

 Agile Planning

 *Kanban board screen shot*
*EPICS*
*User Stories*

## Skeleton Plane

## Surface Plane

Making use of Bootstrap 5.0, I chose to use the Grayscale bootstrap theme from StartBootstrap.com. This decision was made to help reduce the required amount of custom css and javascript that would normally be required.

The Grayscale theme was chosen because I both liked the layout and design of this particular theme. Whilst also matching similarly to the original wireframes.

## Features

- A navbar that provided direction to all the pages across the site. Home, Menu, Enquiries, Profile, My Booking, Register, Log In and Log Out.

- A planned booking form to capture user information for bookings, with CRUD functionality.

## Database Design

The database hosted by ElephantSQL, was designed to capture the essential information given by a user for the site with this particular business to consumer business model. These categories included:
 Title, First Name, Last Name, Email, Phone Number, Booking Date, Start Time, End Time, Address, Dietary Requirements, Booking Size and Requests. 

The plan for the data within the database was to have two seperate views, one for the logged in user so they can view and manage their own booking/s, and also one for the business owner to view all collective bookings from within that database.

## Technologies

- HTML5, CSS3, JavaScript
- Python
- Django
- Bootstrap 5.0
- Postgre ElephantSQL to handle the booking database
- Allauth for new user account registration
- Balsamiq wireframes
- WePik for the bespoke chalkboard themed menu


## Testing

- Bugs

The first bug I encountered building my project was very early in the development cycle. Luckily, it turned out to be a small error and easily corrected once realised. I was met with an error message when trying to install pyscopg. I first tried to find a solution by reviewing posts in Slack to see if other students had similar issues. I spotted a post from with the same problem, and the reply was to install the binary version of pyscopg. Upon installing that variation and reviewing my own code, it was then I discovered that I had been spelling pyscopg incorrectly, and upon correcting my spelling error the installation proceeded as expected.

I also had an issue when setting up template inheretence for my pages. I had mistakenly placed my url's in double curly brackets instead of singular. Which was leading to a parse error when trying to run the pages. With spending longer than I should of reviewing my code to no avail. I reached out to Tutor Assistance, where Holly spotted my error and corrected me on my mistake. After applying Holly's fix, my errors had gone and my pages were working how the should.

I encountered another issue, where after updating my database models and overcoming a brief issue with make migrations. It was the migrate command that followed which required me to turn again to Tutor Assistance after not finding an answer to the validation error, regarding invalid date format. This time John reviewed my code and project files, and since I had no actual database entries yet it was recommended that I reset my SQL database, delete the migration files in my file directory aside from the init.py, and run the make migrations and migrate command again, which corrected my issue.

## Deployment

Site deployment was carried out via Heroku.

## Credit

- Inspiration for The Pizza Project can be attributed to I Scream Tacos. <https://i-scream-tacos.co.uk/> A local mobile food truck based nearby where I live in Bristol, UK. That can be hired to attend local or private events and serve their fresh daily made, traditional Mexican soft shell tacos.

Their business model was used for my project due to it's uniqueness as amethod of serving and delivering quality Mexican food to Bristol and surrounding communities via a second hand repurposed ice cream van. Instead of operating from either a traditional bricks and mortal establishment or a static food trailer, likely to be found within towns and cities, on the roadside or outside sporting/concert venues. By operating out of their taco van they have greater mobility and range than traditional outdoor food vendors which allows them to reach a wider audience.

- Tutor Assistance, 

    Details of issues that requried tutor assistance can be found in the above Bugs section.

- Holly, John, Rebecca & Thomas from Tutor Assistance. Helped me along with issues from template inheritance, model migrations and returning a database views.



