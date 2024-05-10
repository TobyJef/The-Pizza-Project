# The Pizza Project

Welcome to The Pizza Project. Our aim is to provide the local and surrounding communities of Bristol with the freshest and highest quality pizza imaginable, outside of Italy or the pizza hotspots of the USA. We craft out pizza sauce and dough every morning, then load up our mobile pizza truck and head out on the open road where we top and cook our pizzas to order on site. Wether that is at your front door, wedding venue, high street or charity event. If we can drive there, we can cook there. Our pizzas are cooked in a wood fired pizza oven in the back of our pizza truck to ensure that authentic pizza experience.
 
The live link to The Pizza Project website can be found here: *website link here*

- *Home page screen shot here*

This project, based on a fictitous mobile pizza restaurant of my own deisgn but inspired by a company with a similar business model from the local area of my home town in Bristol. Is designed to allow customers to create and log into an account, and to book The Pizza Project mobile truck on a selected date, and have the option to leave a comment on their booking. As well as for the business owner to log into the website as the super user, to manage their bookings and menu.

## Contents

## User Experience

### Strategy Place

Site Goals

### Scope Plane

 Agile Planning

 *Kanban board screen shot*
*EPICS*
*User Stories*

## Skeleton Plane

## Surfance Plane

## Features

## Database Design

## Technologies

- HTML, CSS, JavaScript
- Python
- Django
- Bootstrap
- Bootswatch for free Bootstrap themes. Lux Theme. 
- Allauth for new user account registration 


## Testing

- Bugs

The first bug I encountered building my project was very early in the development cycle. Luckily, it turned out to be a small error and easily corrected once realised. I was met with an error message when trying to install pyscopg. I first tried to find a solution by reviewing posts in Slack to see if other students had similar issues. I spotted a post from with the same problem, and the reply was to install the binary version of pyscopg. Upon installing that variation and reviewing my own code, it was then I discovered that I had been spelling pyscopg incorrectly, and upon correcting my spelling error the installation proceeded as expected.

I also had an issue when setting up template inheretence for my pages. I had mistakenly placed my url's in double curly brackets instead of singular. Which was leading to a parse error when trying to run the pages. With spending longer than I should of reviewing my code to no avail. I reached out to Tutor Assistance, where Holly spotted my error and corrected me on my mistake. After applying Holly's fix, my errors had gone and my pages were working how the should.

I encountered another issue, where after updating my database models and overcoming a brief issue with make migrations. It was the migrate command that followed which required me to turn again to Tutor Assistance after not finding an answer to the validation error, regarding invalid date format. This time John reviewed my code and project files, and since I had no actual database entries yet it was recommended that I reset my SQL database, delete the migration files in my file directory aside from the init.py, and run the make migrations and migrate command again, which corrected my issue.

## Deployment

## Credit

- Inspiration for The Pizza Project can be attributed to I Scream Tacos. <https://i-scream-tacos.co.uk/> A local mobile food truck based nearby where I live in Bristol, UK. That can be hired to attend local or private events and serve their fresh daily made, traditional Mexican soft shell tacos.

Their business model was used for my project due to it's uniqueness as amethod of serving and delivering quality Mexican food to Bristol and surrounding communities via a second hand repurposed ice cream van. Instead of operating from either a traditional bricks and mortal establishment or a static food trailer, likely to be found within towns and cities, on the roadside or outside sporting/concert venues. By operating out of their taco van they have greater mobility and range than traditional outdoor food vendors which allows them to reach a wider audience.

- Tutor Assistance, 

    Details of issues that requried tutor assistance can be found in the above Bugs section.

- Holly from Tutor Assistance. Her quick assistance and observation of where I went wrong with my template inheretence and what was needed to correct my code, which was very much appreciated.

- John from Tutor Assistance. for assisting me with an issue I had with the migrate command to my updated database models. With a brief review of my code and project files. A quick and easy solution was found.

- Rebecca returning booking information 