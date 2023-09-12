Each user story was manually tested in line with intended functionality on both desktop & mobile.

#### Account Registration Tests
| Instruction | Result  |
|--|--|
| Click My Account icon  | There're three links: Register, Login, Useful links |
| Click Register| Redirected to sign up form|
| Click Sign up without filling out the form| The form isn't submitted|
|Fill out the form|All the fields are working properly|
| Click Sign up| The form is submitted and the message in the top right corner informs about confirmation email.|
| Check your email | I received an email with a link to confirm registration|
| Click the link| I clicke dthe link, it opens the website in a new tab, and asks to confirm an email|
| Click confirm| The email is confirmed|

#### Account Login Tests
| Instruction | Result  |
|--|--|
| Click My Account icon  | There're three links: Register, Login, Useful links |
| Click Login| Redirected to login form|
|Enter the wrong password|The form is not submitted|
|Enter the wrong name or email|The form is not submitted|
|Fill out the form correctly|All the fields are working properly|
|Click sign in|Successfully signed in and redirected to home page|

#### Account Logout Tests
| Instruction | Result  |
|--|--|
| Click My Account icon  | There're three links: Register, Login, Useful links |
| Click Logout| Redirected to logout page|
|Click sign out|Successfully signed out|

#### User Navigation Tests
| Instruction | Result  |
|--|--|
| Click Shop Now button  | Redirected to products page |
| Click Cozy Home logo | Redirected home page|
|Click All Products | There are four links: By Price, By Rating, By Category, All Products |
| Click By Price | Redirected to products page, sorted by price from low to high|
| Click By Rating | Redirected to products page, sorted by rating|
| Click All Products | Redirected to products page|
|Click Home Textile | There are three links: Towels, Curtains, All Textile |
|Click Towels | Redirected to products page with towels |
|Click Curtains | Redirected to products page with curtains |
|Click All Textile | Redirected to products page with towels and curtains|
|Click Home Deco | There are three links: Cushions, Vases, All Deco |
|Click Cushions | Redirected to products page with cushions |
|Click Vases | Redirected to products page with vases |
|Click All Deco | Redirected to products page with cushions and vases|
|Click Special Offers | There are three links: New Arrivals, Deals, All Specials |
|Click New Arrivals | Redirected to products page with new arrivals |
|Click Deals | Redirected to products page with deals |
|Click All Specials | Redirected to products page with new arrivals and deals|

#### Wishlist
| Instruction | Result  |
|--|--|
| Login, click Shop now button and tap a heart icon | The product is added to wishlist and I'm redirected to wishlist page |
| On wishlist page click add to bag | The product is added to bag|
|On wishlist page click remove | The product is removed from wishlist |

#### Reviews and ratings
| Instruction | Result  |
|--|--|
| Login, click Shop now button and tap a product image | I'm redirected to product details page |
| Write a review | Text field is working properly|
| Click stars to rate a product | Stars turn yellow|
| Click Post | My review and rating are posted under the product details|

#### Shopping Bag
| Instruction | Result  |
|--|--|
| Click Shop now button and tap a product image | I'm redirected to product details page |
| Click Add to bag button | The product is added to bag|
| Tap bag icon | I'm redirected to shopping bag page|
| Change the quantity of a product in the bag and click Update | The quantity is changed, the subtotal is changed respectively |
| Click Remove | The product is removed from the bag|

#### Checkout
| Instruction | Result  |
|--|--|
| Click Shop now button and tap a product image | I'm redirected to product details page |
| Click Add to bag button | The product is added to bag|
| Tap bag icon | I'm redirected to shopping bag page|
| Click Secure Checkout | I'm redirected to checkout page|
| Fill out the form | All the fields are filled out|
| Enter 4242 4242 4242 4242 card number and any numbers for expiry date, cvc and postcode, and click Complete order| the order is successfully completed|
| Check your email | I got a confirmation email|

#### Subscription
| Instruction | Result  |
|--|--|
| At the bottom of the home page click Subscribe | I'm redirected to Sign in page |
| Log in and click Subscribe again | I'm redirected to subscription form |
| Fill out the form, and click Subscribe | The form is submitted, I'm successfully subscribed. |

#### Account Security Tests

| Test |Result  |
|--|--|
|Non logged in user cannot add a product to a wishlist | True |
|Non logged in user cannot access wishlist| True|
|Non logged in user cannot subscribe for a newsletter | True |
|Non superuser cannot access subscribers list | True|
|Non superuser cannot access Product management page |True|
|Non superuser cannot add products |True|
|Non superuser cannot edit products|True|
|Non superuser cannot delete products|True|