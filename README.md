# Cozy Home

[View the live project here.](https://my-cozy-home-c15fa3106139.herokuapp.com/)

Cozy Home is an E-Commerce website for an online store named “Cozy Home”. Users can see products by categories and purchase them online. Users can register a profile, add products to wishlist, leave reviews, save delivery information, subscribe for a newsletter.

The website is designed to be responsive on a range of devices.

![Am I Responsive screenshot](static/assets/docs/responsive.png)

## Business and Customer Goals

The business model is B2C (Business to Customer) E-Commerce online store. Customers can purchase goods online making individual card payments through the Stripe payment system.

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

Bright green color (#0d5328) is used for "Shop now" and "Add to bag" buttons. 

rgb(255, 0, 85) - is used for wishlist

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

#### Product details page
- Users can tap a product image on products page to see more details about the product.
- On Product details page users can read a description and reviews.
- Users can select the needed quantity and add a product to their shopping bag by clicking "Add to bag" button.
- Users can get back to products page by clicking "Keep shopping" button.
- Users can add a product to their wishlist by clicking "Add to wishlist" button.

![products details page screenshot](static/assets/docs/product-details.png)

#### Reviews and ratings
- Users can read reviews on products details page.
- Users can leave a review and rate a product when they are logged in.

![review and rating form screenshot](static/assets/docs/review-rate.png)
![reviews screenshot](static/assets/docs/reviews.png)

#### Wishlist
- Logged in users can add products to their wishlist.
- Users are being redirected to their wishlist when they add a product.
- Users can tap a heart icon in th etop right corner to view their wishlist.
- When users are on the wishlist page, the icon is red color.
- Users can adjust quantity of a product and add it to a bag.
- Users can remove a product from their wishlist.
- Users can click "Keep shopping" button to get back to products page.
- Users can click "Secure checkout" button to proceed to checkout.
- Users can see a bag icon with total price in the top right corner of the page.
- Users can click a bag icon to get to a shopping bag page.

![wishlist page screenshot](static/assets/docs/wishlist.png)

#### Shopping bag page
- Users can see the products the added to the bag.
- Users can adjust quantity of each product.
- Users can see a product's price and subtotal price, which depends on a product's quantity.
- In the bottom right corner users can see bag total, delivery costs, grand total, and how much they can spend to get free delivery.
- "Keep shopping" button redirects users to products page.
- "Secure checkout" opens checkout page.

![shopping bag page screenshot](static/assets/docs/shopping-bag.png)

#### Checkout page
- Users can see products which they added to thei rshopping bag, their quantity and price.
- Users can see delivery costs and grand total.
- Users can fill out the form with their delivery information.
- Users can click a checkbox to save their delivery information to their profile so they don't have to enter it next time.
- Users can secure enter their card details.
- Users can click "Adjust bag" button to get back to shopping bag page.
- Users can click "Complete order" button to make a purchase. After that their card will be charged.

![checkout form page screenshot](static/assets/docs/checkout.png)
![checkout card form and buttons screenshot](static/assets/docs/checkout-card.png)

#### Sign Up page
- Users can fill out he form to register on the website.

![signup form page screenshot](static/assets/docs/signup.png)

#### Login page
- Users can enter their username or email and password to log into their account.

![Sign in form page screenshot](static/assets/docs/signin.png)

#### Profile
- Users can view their personal profile page.
- Users can see their delivery information if they clicked a checkbox to save it to their profile when making an order.
- On the right side of the page users can view their order history.
- Users can update theur delivery information simply by entering new details and clicking "Update information" button.

![profile page screenshot](static/assets/docs/profile.png)

#### Subscription
- Logged in users can subscribe to a newsletter.
- "Subscribe" button is located at the bottom of the home page.
- If users are not logged in, they are being redirected to login page after clicking "Subscribe" button.
- Users can use the form to enter their name and email.
- After clicking "Subscribe" button under the form, users are successfully subscribed.

![subscription form screenshot](static/assets/docs/subscribe.png)

#### Useful links
- Users can see a navigation link to Useful links page when clicking "My Account" icon.
- On Useful links page users can see and follow links to external resources, such as blog posts, articles or YouTube videos related to website's specialization.
- Users can click "Keep shopping" button to get to products page.

![useful links navigation in menu screenshot](static/assets/docs/useful-nav.png)
![useful links page screenshot](static/assets/docs/useful-links.png)

#### Store Owner functionality
- Store owners can access additional features by clicking "My Account" icon in navigation.
- Store owners have additional access to Product management and Subscribers page

![store owner links in navbar screenshot](static/assets/docs/admin-links.png)

#### Product management
- Store owners can fill the form to add a new product.

![Add product form screenshot](static/assets/docs/add-product-1.png)
![Add product form second screenshot](static/assets/docs/add-product-2.png)

- Store owners can edit or delete products by clicking "Edit" or "Delete" on Products or Product detail page.

![edit product product page acreenshot](static/assets/docs/edit-product.png)
![delete product product detail page screenshot](static/assets/docs/delete-product.png)

#### Newsletter subscribers
- Store owner can see a list of subscribers, their names and emails.

![subscribers list screenshot](static/assets/docs/subscribers.png)


### Future features

- Users can check a box on checkout page to subscribe for a newsletter.
- Users can recover password.
- Store owner can moderate reviews.
- Store owner can send a newsletter filling the form on the website.

## Marketing

### Business model
This project is based on E-Commerce B2C business model.
Customers can purchase goods online making individual card payments through the Stripe payment system.

### Purpose of the application
Cozy Home is a website for an online store. The main goal of the website is to allow users to view the products and to buy them online. Also the website makes it possible for users to add products to a wishlist, to save delivery information on a personal profile page, to subscribe for a newsletter, to read and leave reviews.

### Marketing strategies
Free web marketing strategies are used for this E-Commerce project.
- SEO and content marketing
- Social media marketing (Facebook)
- Email marketing (Newsletter subscription)

#### SEO
Search Engine Optimization (SEO) techniques are used in this project to  optimize the web page and content for better search engine rankings.
- Keywords and descriptive meta tags
- External links with rel attributes and aria-labels
- robots.txt
- sitemap.xml

#### Facebook business page.
- Customers can easily locate Facebook page link at the bottom of the home page.
- Customers can tap the link to open store's facebook business page.
- Customers can follow the page to be regularly informed about new arrivals or special offers. This will increase customers' awareness and loyalty. 

Tap [here](https://www.facebook.com/mycozyhomehere/) to see the page on Facebook.

![Facebook page screenshot](static/assets/docs/facebook-page.png)

#### Newsletter subscription

- Users can subscribe for a newsletter by filling the form on the website. Store owners can email newsletter informing customers about new arrivals or special offers. It will help to gain new customers or retain existing ones
- After implementing "Future features" section, users will be able to check a box to subscribe for a newsletter while checking out. More users will be willing to subscribe as it doesn't take time and additional efforts to fill out the form. That will increase customers' loyalty. 

![subscribe button in footer screenshot](static/assets/docs/footer.png)
![subscription form screenshot](static/assets/docs/subscribe.png)

## Testing
- **Responsiveness**
[Am I responsive](https://github.com/konstanciaa/cozy-home/blob/main/static/assets/docs/responsive.png)
- **Lighthouse** [Result](https://github.com/konstanciaa/cozy-home/tree/main/static/assets/docs/validation/lighthouse.png/)
- **Validation** (HTML, CSS, Python)
[Validation results](https://github.com/konstanciaa/cozy-home/tree/main/static/assets/docs/validation)
- **Bugs**

Subscription form wouldn't submit. The issue was with user's id. There was IntegrityError at /profile NOT NULL constraint failed. This [Stackoverflow post](https://stackoverflow.com/questions/66662129/integrityerror-at-profile-not-null-constraint-failed-tutorapp-profile-user-id) helped me to resolve the bug. 

- **User Stories Testing** and **Features Testing** can be found [here](https://github.com/konstanciaa/cozy-home/tree/main/docs/testing.md)


## Technologies Used
- [HTML](https://en.wikipedia.org/wiki/HTML) - used for creating templates
- [CSS](https://en.wikipedia.org/wiki/CSS) - used for custom styling
- [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/) - CSS Framework used for developing responsive and mobile-first websites
- [JavaScript](https://www.javascript.com/) - programming language used to make web pages interactive
- [Python](https://www.python.org/) - high-level general-purpose programming language used to write the code for the project
- [Django](https://www.djangoproject.com/) - Python framework used to build the project
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html) - Django pre-built package used for authentification
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/index.html#) - Django app used to manage Django forms
- [django-storages](https://django-storages.readthedocs.io/en/latest/) - Django library used to connect the project to Amazon S3 Bucket
- [Amazon S3 bucket](https://aws.amazon.com/s3/) - AWS web-based cloud storage service used for storing static and media files
- [Heroku](https://dashboard.heroku.com/apps) - cloud platform used for deployment
- [Stripe](https://stripe.com/en-gb) - used to take payments
- [Font Awesome](https://fontawesome.com/) - used for icons
- [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools) - used for manual testing and responsiveness
- [GitHub](https://github.com/) - used to host repo
- [Git](https://git-scm.com/) - used for version control
- [Gitpod](https://www.gitpod.io/) - used as IDE
- [Miro](https://miro.com/) - used to create ERD and wireframes
- [ElephantSQL](https://www.elephantsql.com/) - as database
- [favicon.io](https://favicon.io/) - used for favicon
- [Am I Responsive](https://ui.dev/amiresponsive/) - used for responsive image mockup
- [Django Secret Key Generator](https://djecrety.ir/) - used to generate secret keys for the project
- [Canva](https://www.canva.com/) - used for resizing images and picking the colors from the images
- [Font Awesome](https://fontawesome.com/) - was used for icons in navbar, footer and on the buttons "Secure checkout", "Keep shopping".

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
- Uncomment previous database code in settings.py and comment out the new lines. So we don't push our database link.
- Deploy an app

### Connecting Heroku to Github

By connecting Heroku to Github the application will automatically deploy the latest code to Heroku.

- In heroku app, open app, in "Deploy" tab, under the "Deployment method" setting select "GitHub"
- Search for repository and click "Connect"
- Choose "Enable Automatic Deploys"
- Modify `settings.py` to use environment variables
- Add the environment variables to Heroku
- Confirm Heroku to Github connection

### The Development Environment

Set up a local development environment so that you don't have to change any settings to run the project in gitpod.

- Modify `settings.py`:
  - create a new "development" variable
  - set "Debug" to development
  - modify the "DATABASES" configuration and add an if statement
  - add a "localhost" as an ALLOWED_HOST if development = True
  - else use the HEROKU_HOSTNAME environment variable


### Config vars

A series of config vars have to be created in Heroku, to conect the app to Django, AWS, Stripe and Gmail.

The final list of config vars in Heroku can be seen below

![Configuration variables Heroku screenshot](static/assets/docs/config-var.png)

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
- Register an account
- Search S3 service
- Create a bucket
- Set Object Ownership to ACLs enabled (Bucket owner preferred)
- Set CORS configuration to `[
{
"AllowedHeaders": [
"Authorization"
],
"AllowedMethods": [
"GET"
],
"AllowedOrigins": [
"*"
],
"ExposeHeaders": []
}
]`
- For the Access control list (ACL) section, click edit and enable List for Everyone (public access) and
accept the warning box.

- Identify and Access Management (IAM)
  - Create group.
  - Create policy.
  - Attach policy. To attach the policy, on the sidebar, click User Groups. Select your group, go to the permissions tab, open the Add permissions dropdown, and click Attach policies. Select the policy and click Add permissions at the bottom.

- Retrieve access keys
  - Go to IAM and select 'Users'
  - Select the user for whom you wish to create a CSV file.
  - Select the 'Security Credentials' tab
  - Scroll to 'Access Keys' and click 'Create access key'
  - Select 'Application running outside AWS', and click next
  - On the next screen, you can leave the 'Description tag value' blank. Click 'Create Access Key'
  - Click the 'Download .csv file' button.

## References and Credits
- Code Institute's walkthrough project [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1) was used as a boilerplate for this project.
- All images are taken from [Pexels](https://www.pexels.com/)
- [codepiep](https://youtu.be/A8rarkE0TKQ?si=e786WPFV2NEdOo5M) YouTube tutorial helped me to implement wishlist functionality.
- [Coding Stuff](https://youtu.be/reFJ9hBLFUY?si=upL6Vv_IbVSXQ6dZ) and [David Gilliam](https://youtu.be/3VW1ws88MKc?si=h3pPvE80rkfs9Bba) YouTube tutorials helped me to implement review and rating functionalities.
- [Python Lessons](https://youtu.be/wl4Yxo5_Cgw?si=Gk00Y6rJjsd2yGNB) and [KenBroTech](https://youtu.be/hWtlskOaFNI?si=4TGFnWy9YDDdXIit) YouTube tutorials helped me to implement newsletter subscription functionality.

### Acknowledgements

#### Brian O'Hare
My mentor who provided me with constructive feedback and guidance throughout the project.

#### The tutors at Code institute
To all the tutors in CI, thank you for your help. Special shout outs to Gemma and Oisin.
