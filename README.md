# Telecom Carrier API
This project is a RESTful API developed in Python using the Flask framework to manage available phone numbers in an inventory. The API allows CRUD (Create, Read, Update, Delete) operations on phone numbers, following the agreed specifications.

## Technologies Used

• Python (version 3.9)

• Flask (web framework)

• SQLAlchemy (ORM for database)

• PostgreSQL (database)

• Docker (containerization)

• Docker Compose (container orchestration)

## How to Run the Project

### Prerequisites

• Docker (version 19 or higher)

• Docker Compose (version 1.25 or higher)

• Postman or Insomnia (for API testing)

### Steps to Run

#### 1. Clone the repository:

``` bash
git clone https://github.com/your-username/telecom-carrier.git
```

#### 2. Enter the project directory:
```bash
cd telecom-carrier
```

#### 3. Start the containers:
```bash
docker-compose up -d
```

This will:

• Build the Docker image for the Flask application.

• Start the PostgreSQL database.

• Run the Flask application on port 5000.

#### 4. Create the database tables:

After the containers are up, you need to create the database tables.

• Access the application container:

```bash
docker-compose exec web bash
```

• Inside the interactive terminal start the Flask database:

```bash
flask db init
```

• Now, manage migrations with:

```bash
flask db migrate -m "Your migration description"
```

• Apply the changes to the database:

```bash
flask db upgrade
```

• Exit the terminal with:

```bash
exit
```

## API testing

The API will be available at http://localhost:5000.

### API Endpoints

• GET /numbers: Returns all phone numbers.

• GET /numbers/{id}: Returns a specific phone number.

• POST /numbers: Creates a new phone number.

• PUT /numbers/{id}: Updates an existing phone number.

• DELETE /numbers/{id}: Deletes a phone number.