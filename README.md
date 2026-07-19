# Foundry
#### Video Demo:  [Video](https://youtu.be/a3MynEh13rU)
#### Description:


I made a web application called Foundry. It is built with Flask. It helps users save, review and reuse SVG code snippets. The main purpose of Foundry is to give users a place to store their SVG files or code snippets.

They do not have to keep searching for them through folders or old projects or notes on their computers. If they need the icon or graphic again they can easily store them and upload the code to Foundry.

I chose this project because SVGs are commonly used in websites and applications. They are scalable, lightweight and easy to customize with code. However when working on projects it can become difficult to keep track of different SVG icons, illustrations, logos and UI elements.

Foundry solves this problem by letting users create an account where they can add SVGs to their collection. They can add the used ones and view them anytime as previews. Then they can copy the SVG code where needed.

Foundry includes a register option and a login system. Each user has their private dashboard and other people cannot modify it. All SVGs are displayed in a dashboard. Each SVG is reviewed in a card. Used by an iframe with both its name and its visual preview.

There is also an option that can be expanded to see the SVG code and copy it. I built Foundry because I faced the problem. I used SVGs often in websites because they were easy to scale and manage.

Then I used to forget where I kept them. It took longer for me to find them. So I thought I could make a project on it. It could also be my final project. I made it because it was an application.

Foundry uses Python with Flask for the backend. I used SQLite for the database and HTML and CSS for content. I used a template engine with Flask for templates. Passwords are securely stored in hashed password hashing of plain text.

I also used apology and error messages to tell the users what is wrong.

Features of Foundry include:

\* The first main feature is user authentication. Users can register with a username, email and password. The password is hashed before being stored in the database.

\* The second main feature is the SVG storage. Users can add SVGs by providing a name and code.

\* The third feature is the dashboard. The dashboard displays all the SVGs belonging to the logged-in user.

\* The fourth feature is copying the SVG codes. Since the goal of Foundry is to help users reuse SVG each SVG includes a copy button.

Files and Structure of Foundry:

\* app.py contains the Flask application.

\* Helpers.py contains helper functions used by the application.

\* The templates folder contains the HTML templates used by Flask.

\* The static folder contains the CSS file used to style the website.

\* The SQLite database stores user. Svg data.

Design Choices of Foundry:

\* One important design choice was to store SVG code in the database instead of storing uploaded files in a folder.

\* Another design choice was to keep the authentication system simple.

\* I also chose to make the interface minimal.

Future Improvements of Foundry:

\* In the future I would like to add organization features, such, as tags, folders, search and filtering.

\* I would also like to add an edit feature so users can update saved SVG names or code after uploading them.

\* Another possible improvement is allowing users to download saved SVGs as.svg files.

Overall Foundry is a useful Flask application that combines user authentication, database storage, dynamic templates and frontend interaction into one complete project.
