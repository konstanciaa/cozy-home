# Cozy Home

[View the live project here.](https://my-cozy-home-c15fa3106139.herokuapp.com/)

Cozy Home is an E-Commerce website for an online store named “Cozy Home”. Users can see products by categories and purchase them online. Users can register a profile, add products to wishlist, leave reviews, save delivery information, subscribe for a newsletter.

The website is designed to be responsive on a range of devices.

![Am I Responsive screenshot](static/assets/docs/responsive.png)

## Business and Customer Goals

The business model is B2C (Business to Customer). Customers can purchase goods online making individual card payments through the Stripe payment system.

#### Overview
Cozy Home is a website for an online store. The main goal of the website is to allow users to view the products and to buy them online. Also the website makes it possible for users to add products to a wishlist, to save delivery information on a personal profile page, to subscribe for a newsletter, and to read and leave reviews.

#### Site User
- Someone who is an interior designer.
- Someone whose hobby is interior design.
- Someone looking for new bed linen or towels.
- Someone who prefers online shopping.

#### Goals for the website
- To allow customers to view the products, their images, description, price.
- To allow customers to add products to a wishlist.
- To allow customers to add products to a shopping bag.
- To allow customers to make secure online payment.
- To allow customers to receive a confirmation email after checkout.
- To allow customers to subscribe for a newsletter.
- To allow customers to save their delivery information on a personal profile page.
- To allow store owner to add, edit and delete products.
- To allow store owner to view the list of subscribers.


### User Stories

#### Completed User Stories

Click on a user story to see the details.

1. [USER STORY: List of products](https://github.com/konstanciaa/cozy-home/issues/1)

2. [USER STORY: Product details](https://github.com/konstanciaa/cozy-home/issues/2)

3. [USER STORY: Special offers](https://github.com/konstanciaa/cozy-home/issues/3)

4. [USER STORY: View total](https://github.com/konstanciaa/cozy-home/issues/4)

5. [USER STORY: Wish list](https://github.com/konstanciaa/cozy-home/issues/5)

6. [USER STORY: Register an account](https://github.com/konstanciaa/cozy-home/issues/6)

7. [USER STORY: Login and logout](https://github.com/konstanciaa/cozy-home/issues/7)

8. [USER STORY: Email confirmation](https://github.com/konstanciaa/cozy-home/issues/9)

9. [USER STORY: User profile](https://github.com/konstanciaa/cozy-home/issues/10)

10. [USER STORY: Sort products by price](https://github.com/konstanciaa/cozy-home/issues/11)

11. [USER STORY: Sort a category](https://github.com/konstanciaa/cozy-home/issues/12)

12. [USER STORY: Search for a product](https://github.com/konstanciaa/cozy-home/issues/13)

13. [USER STORY: Select quantity of a product](https://github.com/konstanciaa/cozy-home/issues/14)

14. [USER STORY: View bag](https://github.com/konstanciaa/cozy-home/issues/15)

15. [USER STORY: Adjust quantity of items in bag](https://github.com/konstanciaa/cozy-home/issues/16)

16. [USER STORY: Enter payment details](https://github.com/konstanciaa/cozy-home/issues/17)

17. [USER STORY: Secure payment details](https://github.com/konstanciaa/cozy-home/issues/18)

18. [USER STORY: Order confirmation](https://github.com/konstanciaa/cozy-home/issues/19)

19. [USER STORY: Email confirmation](https://github.com/konstanciaa/cozy-home/issues/20)

20. [USER STORY: Add products](https://github.com/konstanciaa/cozy-home/issues/21)

21. [USER STORY: Update products](https://github.com/konstanciaa/cozy-home/issues/22)

22. [USER STORY: Delete products](https://github.com/konstanciaa/cozy-home/issues/23)

23. [USER STORY: Leave a review](https://github.com/konstanciaa/cozy-home/issues/24)

24. [USER STORY: Read reviews](https://github.com/konstanciaa/cozy-home/issues/26)

25. [USER STORY: Subscribe for a newsletter](https://github.com/konstanciaa/cozy-home/issues/27)

26. [USER STORY: View the wishlist](https://github.com/konstanciaa/cozy-home/issues/29)

27. [USER STORY: Remove from wishlist](https://github.com/konstanciaa/cozy-home/issues/30)

28. [USER STORY: Add to bag from wishlist](https://github.com/konstanciaa/cozy-home/issues/31)

29. [USER STORY: List of subscribers](https://github.com/konstanciaa/cozy-home/issues/32)


#### Future features user stories

1. [USER STORY: Recover password](https://github.com/konstanciaa/cozy-home/issues/8)

2. [USER STORY: Moderate reviews](https://github.com/konstanciaa/cozy-home/issues/25)

3. [USER STORY: Check a box to subscribe](https://github.com/konstanciaa/cozy-home/issues/28)


## UI/UX Design

### Color Scheme

There is a big image of a cozy bedroom on the home page. The page gives an idea of what is the website about and sets an appropriate mood.

The color scheme comes mainly from the home page image.

![Color scheme screenshot](static/assets/docs/color-scheme.png)

I added bright green color (#0d5328) for "Shop now" and "Add to bag" buttons. 

rgb(255, 0, 85) - for wishlist

### Wireframes

Home page
![Home page wireframe screenshot](static/assets/docs/home-page-frame.png)

All products page
![Products page wireframe screenshot](static/assets/docs/all-products-frame.png)

Product details page
![Product detail page wireframe screenshot](static/assets/docs/product-detail-frame.png)

Shopping bag page
![Bag page wireframe screenshot](static/assets/docs/bag-frame.png)

## Database Design
![database models screenshot](static/assets/docs/database-models.png)


## Features

#### User based Features Implemented

- **Users can** register on a website
- **Users can** log into their account
- **Users can** log out of their account
- **Users can** view all the products and their details
- **Users can** search products on the website
- **Users can** sort the products by categories, price, rating
- **Users can** read and leave reviews
- **Users can** add products to wishlist
- **Users can** delete products from wishlist
- **Users can** add products to bag
- **Users can** add products from wishlist to bag
- **Users can** adjust quantity of products in their wishlist
- **Users can** adjust quantity of products in their shopping bag
- **Users can** make a secure online payment
- **Users can** subscribe for a newsletter
- **Users can** save their delivery information on their profile
- **Users can** update their personal information on their profile


#### User Restrictions
- **Users cannot** access the subscription form until they sign up or login
- **Users cannot** access wishlist until they sign up or login
- **Users cannot** leave a review until they sign up or login
- **Users cannot** see other users profiles
- **Users cannot** see other users wishlists
- **Users cannot** see subscribers list
- **Users cannot** add, edit or delete products

#### Business owner based Features implemented

- **Business owner can** add products **(Create)**
- **Business owner can** view all products **(Read)**
- **Business owner can** edit products **(Update)**
- **Business ownern can** delete products **(Delete)**
- **Business owner can** view the list of subscribers

### Website Features

#### Navigation

- The navigation is located at the top of the page. It shows the store name in the left corner: COZY HOME that links to home page.
- The other navigation links are: All Products, Home Textile, Home Deco, Special Offers which link to different categories of products.
- A search bar is located above the product categories link.
- Wishlist, My Account and Bag icons function as links to these pages.

![navigation screenshot](static/assets/docs/navbar.png)

#### Home page
- Home page displays a photo of a cozy bedroom.
- The big green button calls to action "Shop Now".
- After clicking the button, users are being redirected to products page.
- The information about free delivery condition is at the top of the image, between navigation links and hero image.

![home page screenshot](static/assets/docs/home-page.png)

#### Footer
- Users can see a Subscribe button which redirects them to subscription page. If the user is not registered or not logged in, they are being redirect to login page.
- The Follow button opens the store's Facebook page in a new tab.

![footer screenshot](static/assets/docs/footer.png)

#### Products
- User can see all products, their names, prices, categories, rating under images.
- The heart icon under each product enables users to add a product to a wishlist. If the user isn't logged in, they are being redirected to login page first.
- Users can tap a product image to see more details about the product.
- "Sort by..." bar ebnables users to sort products by categories, price, name, rating in different directions.

![products page screenshot](static/assets/docs/all-products.png)



### Future features

## Marketing
ECommerce business model. Purpose of the appliication. B2C. Marketing Strategies. Facebook

#### Facebook business page.

Tap [here](https://www.facebook.com/mycozyhomehere/) to see the page on Facebook.

![Facebook page screenshot](static/assets/docs/facebook-page.png)


## Testing
- Responsiveness
- Browser Compatibility
- Bugs (resolved and unresolved)
- Lighthouse
- Validation (HTML, CSS, Python)
[Validation results](https://github.com/konstanciaa/cozy-home/tree/main/static/assets/docs/validation)

- User Stories Testing
- Features Testing

## Technologies Used
Frameworks, Libraries, Programs

## Procedures

### Deployment
The project's repo was hosted on GitHub and deployed on Heroku

#### Create a database

- Log in to [ElephantSQL.com](https://www.elephantsql.com/) to access dashboard
- Create New Instance
- Copy the database URL and add it to Heroku config var

#### Heroku

[Heroku](https://id.heroku.com/login)

- Sign up / login to [Heroku](https://id.heroku.com/login) website
- Create new app
- Add the config var DATABASE_URL, and for the value, copy in your database url from ElephantSQL.

#### Installing Project Requirements
- In the terminal, install dj_database_url and psycopg2, both of these are needed to connect to the external database. `pip3 install dj_database_url==0.5.0 psycopg2`
- Update requirements.txt file with the newly installed packages. `pip freeze > requirements.txt`
- In settings.py file, import dj_database_url underneath the import for os.
- Scroll to the DATABASES section and update it to the following code, so that the original connection to sqlite3 is commented out in order to connect to the new ElephantSQL database instead. Paste in the ElephantSQL database URL in the position indicated.
`     
 DATABASES = {
     'default': dj_database_url.parse('your-database-url-here')
 }
`

- In the terminal, run the showmigrations command to confirm you are connected to the external database. `python3 manage.py showmigrations`

- Migrate your database models to your new database.

- Create a superuser for your new database. `python3 manage.py createsuperuser`

- Install gunicorn

- Freeze requirements 

- Create Procfile

- Disable collectstatic on Heroku

- Add the hostname of Heroku app to ALLOWED_HOSTS in settings.py

- Deploy an app


### Connecting Heroku to Github

By connecting Heroku to Github the application will automatically deploy the latest code to Heroku.

- in heroku app, open app, in "Deploy" tab, under the "Deployment method" setting select "GitHub"
- search for repository and click "Connect"
- choose "Enable Automatic Deploys"
- modify `settings.py` to use environment variables
- add the environment variables to Heroku
- confirm Heroku to Github connection

### The Development Environment

Set up a local development environment so that you don't have to change any settings to run the project in gitpod.

- modify `settings.py`:
  - create a new "development" variable
  - set "Debug" to development
  - modify the "DATABASES" configuration and add an if statement
  - add a "localhost" as an ALLOWED_HOST if development = True
  - else use the HEROKU_HOSTNAME environment variable
- add a new environment variable set to TRUE
- restart workspace
- run server

### Config vars

A series of config vars have to be created in Heroku, to conect the app to Django, AWS, stripe and email.

The final list of config vars in Heroku can be seen below

### Github

#### Create a new repository

- Log into [GitHub](https://github.com/)
- On the 'Repositories' tab click 'New'
- Name the repository and click 'Create repository'

#### Forking

- Sign into Github and go to my [repo](https://github.com/konstanciaa/cozy-home)
- Press the "Fork" button the top right corner of page
- Click "Create fork"

#### Cloning

- Sign in to Github and go to my [repo](https://github.com/konstanciaa/cozy-home)
- Above the list of files click "Code"
- Select HTTPS, SSH or Github CLI, then click the copy button to get the URL
- Open your IDE of choice
- Type "git clone" and then paste the URL you copied
- Press Enter

[Cloning a repository In GitHub documantation](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)


### AWS S3 Bucket Creation

### Stripe Configuration

## References and Credits
Boutique Ado. 

Media and Content. Pexels

