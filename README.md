# I teach French: a free resources website for teachers of French

As a teacher, we spend a lot of time preparing resources that are engaging for students to support teaching and learning. A good resource can make a real difference in helping students understanding concepts. However, creating resources is very time consuming for teachers who also need to prepare and deliver lessons, as well as mark students' work. 

## UX

### Project goals

I Teach French aims to provide free, easily accessible downloadable resources for teachers to use in their lessons. The search function allows users to enter key words relating to the topic they want to work on and quickly assess the nature of the resource with an image, the language skill, the level and a description in French and English, before they download it.There is a possibility to leave a donation of 5€ for users who think that they have found some value in the resources. Similar sites that exist today operate either on a subscription basis (frenchteacher.net), or they charge for resources (tes.com/teaching-resources) or they are riddled with adverts which make for an unpleasant user experience (fr.islcollective.com).

### User stories

As a user of I Teach French
* I can access a collection of free downloadable teaching resources.
* I can search the collection with keywords in French or English.
* I can visually assess the nature of the resource.
* I can download the resources in one click.
* I can create an account and receive a personalised welcome when I log in.
* I can make a donation of €5 via Stripe if I want to encourage the creation of more material.

As the owner of the site
* I can upload files to the site and share them with a community of teachers.
* I can receive donations via Stripe from users.
* I can store the resources that I have created online and easily access them when needed.

### design choices

The design makes it straightforward for users to access the main feature of the site, the resources. Once their account is created, they land on the home page where they have 2 options, go to the collection or donate, they can do so via the navbar or via in-text links. If they want to donate they are redirect to Stripe's checkout where they are invited to enter their card's details to donate 5€. If they go to the resources they can scroll through the bank of resources or enter key words in the search bar to quickly access resources that might be of interest, should they find something of interest they can just click on the download button. They can go back to the home page at any time by clicking on I Teach French in the bar. The bar and the reources page are responsive and display well on mobiles tablets and laptops. The color scheme is pure black and white for ease of reading and the site's background displays a photo of Paris to match with the site's target language.


## Features

* Home page
    * The user is invited to register or login
* Sign up page
    * The user is invited to provide a username and a password to create a profile.
* Log in page
    * The user is required to enter their username and a password
*  Profile page
    * Here, the user can see a personalised welcome message, he is invited to go to the resources collection or to donate.
* Resources page
    * The user can scroll through the resource collection or use the search function to acess a specific resource, this can be done in French or English
* Donations page
    * The user is given the opportunity to donate 5€ to encourage resources creation and sharing, if they change their mind they can return to the main site via the navbar, if they choose to go forward with their donation, they are redirect to the Stripe checkout page where they can enter their card details. After a successful transaction they are redirected to the success page.

## Features left to implement

* Users' rating of resources
* User's comments on resources

## Technologies used

* HTML 5
* CSS 3
* [Bootstrap](https://www.python.org/)
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/) (framework)
* [Javascript] (access to stripe checkout)
* [Google Fonts](https://fonts.google.com/) (Lobster)
* [Font Awesome](https://fontawesome.com/) (all icons)
* [JQuery](https://jquery.com/) (triggering si)
* [Github](https://github.com/) (code hosting platform for version control)
* [Gitpod](https://gitpod.io/) (development environment) 
* [Stripe](https://stripe.com/) (for payment)
* [Heroku](https://heroku.com/) (platform where the site is deployed)

## Testing

* Code validity:

HTML has been validated using [W3 validator](https://validator.w3.org/) and formatted using [Freeformater](https://www.freeformatter.com/).
CSS has been validated using [W3 CSS validator](http://jigsaw.w3.org/css-validator/validator).
Lightouse testing from Chrome developer's tools returned positive results.

* Functionalities:


## Deployment to Heroku and AWS

* pip 3 freeze --local > requirements.text
* create procfile Procfile > web: gunicorn I_Teach_French.wsgi
* on AWS services use S3 and IAM for your static files
*

## Credits

### Media

* All medias have been created by myself
* The background picture used on the site is Jibs-breizh from [Pixabay](https://pixabay.com/)

### Acknowledgements

* code used:
* Boutique Ado project by Code Institute
* Stripe checkout by Anthony Herbert at Pretty Printed on Youtube

### Thank you

* To Everyone at Code Institute for their patience!
* To the dedicated team of tutors who are always helpful


