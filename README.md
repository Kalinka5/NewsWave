<div style="width: 100%;">
  <img src="hello.svg" style="width: 100%;" alt="Click to see the source">
</div>

# NewsWave

NewsWave is a web application built using Django for the backend and React for the frontend. It provides a platform for users to read and manage news articles. The project includes JWT authentication, user registration, news listing, category filtering, and CRUD operations for news articles.

## Features

- User Authentication: Users can register and log in to the site using JWT authentication.

- News Listing: Users can view a list of news articles, with 3 articles displayed per page.

- Pagination: The news articles are paginated, allowing users to navigate between pages.

- Category Filtering: Users can filter news articles by category, including "Important," "World," "Sport," "Games," and "Fashion."

- Create News (Manager Only): Manager users have the ability to create new news articles using the "Create News" button in the navigation bar.

- Edit News (Manager Only): Manager users can edit news articles, updating their title, description, and images.

## Setup Instructions

### Backend Setup (Django)

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/NewsWave.git
   ```
2. Create a virtual environment and activate it:
   ```bash
   pipenv shell
   ```
3. Install the required dependencies:
   ```bash
   pipenv install
   ```
4. Navigate to the backend repository:
   ```bash
   cd NewsWave/backend
   ```
5. Apply migrations to set up the database:
   ```bash
   python manage.py migrate
   ```
6. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup (React)

1. Open a new terminal window and navigate to the frontend directory:
   ```bash
   cd NewsWave/frontend
   ```
2. Install the required npm packages:
   ```bash
   npm install
   ```
3. Start the React development server:
   ```bash
   npm start
   ```
4. Access the web application in your browser at http://localhost:3000.

# Sceenshots
![image](https://github.com/Kalinka5/NewsWave/assets/106172806/cd63fdac-05ad-482c-af2b-7df93672b981)

___

![image](https://github.com/Kalinka5/NewsWave/assets/106172806/bb6a087b-7967-403d-a913-eb7ebb837961)

___

![image](https://github.com/Kalinka5/NewsWave/assets/106172806/a641d691-20a3-44c5-986b-f446f958108c)

___

![image](https://github.com/Kalinka5/NewsWave/assets/106172806/6757f84f-fd01-4baa-8a01-d5849af74a2a)

___

![image](https://github.com/Kalinka5/NewsWave/assets/106172806/0ed2f00b-7f27-4b00-86ce-ed113d0e6a02)

## Usage

- **Register**: Users can register for an account by clicking on the "Register" link and providing their details.

- **Login**: Existing users can log in using their credentials.

- **News Listing**: Users can browse through the list of news articles, navigate between pages, and click on categories to filter news.

- **Create News (Manager)**: Manager users can click on the "Create News" button in the navigation bar to add new articles.

- **Edit News (Manager)**: Manager users can edit news articles by clicking on the edit icon next to each article. They can update the title, description, and images.

## Contributors

- Daniil Kalinevych (@Kalinka5)

Feel free to contribute to this project by creating issues and pull requests.
