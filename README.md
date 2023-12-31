<div style="width: 100%;">
  <img src="hello.svg" style="width: 100%;" alt="Click to see the source">
</div>

<h1 align="center">:✧  📺  𝒩𝑒𝓌𝓈𝒲𝒶𝓋𝑒  📺  ✧:</h1>

<b><i>NewsWave</i></b> is a web application built using <b>Django</b> for the backend and <b>React</b> for the frontend. It provides a platform for users to read and manage news articles. The project includes <b>JWT authentication</b>, user registration, news listing, category filtering, and CRUD operations for news articles.

## Features 🌟

- **User Authentication**: 👤 Users can register and log in using JWT authentication for secure access.

- **News Listing**: 📰 Browse through a paginated list of news articles with categories.

- **Category Filtering**: 🗂️ Filter news articles by categories like Important, World, Sport, Games, and Fashion.

- **Create News (Manager)**: 📝 Managers can create new news articles with titles, descriptions, and images.

- **Edit News (Manager)**: ✏️ Managers can edit existing news articles, updating title, description, and images.

- **Throttling**: ⏳ Implement throttling to control API usage: anonymous users are limited to 2 requests per minute, while authenticated users can make up to 30 requests per minute.

- **Responsive Design**: 📱 Enjoy a responsive and user-friendly design for both desktop and mobile devices.

## Setup Instructions 📄

### Backend Setup (Django) 🐍

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

### Frontend Setup (React) 🚀

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

## Usage 💻

- **Register**: 👤 Users can register for an account by clicking on the "Register" link and providing their details.

- **Login**: 🔑 Existing users can log in using their credentials.

- **News Listing**: 📰 Users can browse through the list of news articles, navigate between pages, and click on categories to filter news.

- **Create News (Manager)**: 📝 Manager users can click on the "Create News" button in the navigation bar to add new articles.

- **Edit News (Manager)**: ✏️ Manager users can edit news articles by clicking on the edit icon next to each article. They can update the title, description, and images.

## Sceenshots 🖼️
![image](https://github.com/Kalinka5/NewsWave/assets/106172806/cd63fdac-05ad-482c-af2b-7df93672b981)

___

![image](https://github.com/Kalinka5/NewsWave/assets/106172806/bc2b62fc-666d-4013-b66f-2efb86312143)

___

![image](https://github.com/Kalinka5/NewsWave/assets/106172806/a641d691-20a3-44c5-986b-f446f958108c)

___

![image](https://github.com/Kalinka5/NewsWave/assets/106172806/6757f84f-fd01-4baa-8a01-d5849af74a2a)

___

![image](https://github.com/Kalinka5/NewsWave/assets/106172806/0ed2f00b-7f27-4b00-86ce-ed113d0e6a02)

## Contributors 👏

- Daniil Kalinevych (@Kalinka5) ✨

Feel free to contribute to this project by creating issues and pull requests.
