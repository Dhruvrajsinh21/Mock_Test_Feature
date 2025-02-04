# Mock_Test_Feature

![image](https://github.com/user-attachments/assets/7e0238c8-02ef-437e-9fa5-ab211eff41e3)
 
![image](https://github.com/user-attachments/assets/90bcd1ca-e45e-4704-aba3-7f5a6b13979b)


![image](https://github.com/user-attachments/assets/7176ab54-bbd2-420c-b239-adb4fdae3307)

# Mock Test API

This API allows users to start a mock test and submit answers for various questions.

## Endpoints

### 1. **User Registration**

**POST** `/api/register/`

Registers a new user by providing a username and password.

#### Request:
```json
{
    "username": "user123",
    "password": "password123"
}
Response:
```json
{
    "message": "User registered successfully"
}
```
2. User Login
POST /api/login/

Logs in an existing user by providing a username and password.

Request:
```json
{
    "username": "user123",
    "password": "password123"
}
```
Response:
```json
{
    "message": "Login successful"
}
```
3. Start Mock Test
GET /api/start_mock_test/

Starts a mock test for the user identified by the user query parameter.

Request Example:
```http
GET /api/start_mock_test/?user=1
```
Response:
```json
{
    "id": 1,
    "user": 1,
    "questions_answered": [],
    "start_time": "2025-01-21T03:21:24.343121Z"
}
```
4. Submit Answer
POST /api/submit_answer/{question_id}/

Submit an answer to a specific question.

Request Example:
```json
{
    "user_answer": "42"
}
```
Response:
```json
{
    "message": "Answer submitted successfully"
}
```

Models
MockTest: Stores mock test information (user, questions answered, start time).
Answer: Stores the user's answers to mock test questions.
Running the Project
Install dependencies: pip install -r requirements.txt
Run migrations: python manage.py migrate
Start the server: python manage.py runserver

The output of the start_mock_test endpoint will depend on the following scenarios:

If a user is provided (either by query parameter or default):

The MockTest object will be created or retrieved for that user.
If the MockTest is newly created, the system will add a random set of questions (e.g., 10 questions) that have not been answered by the user yet.
The MockTest object will be returned with the user and the questions they are to answer.
If the user already has a MockTest:

The system will return the existing MockTest object with the questions the user has already answered.
Example of Output:
Assume that the user has not yet started their mock test, and the system adds 10 questions to the mock test. The output might look like this:

```json
{
    "id": 1,
    "user": 1,
    "questions_answered": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ],
    "start_time": "2025-01-21T03:21:24.343121Z"
}
```
Where:

id: The ID of the MockTest (could be auto-generated).
user: The ID of the user associated with the mock test.
questions_answered: A list of question IDs that the user is assigned to answer.
start_time: The timestamp when the mock test started.
If the user already has answered some questions, the questions_answered list will only contain the IDs of the questions they have already answered. If no new questions are added (i.e., all questions have been answered already), the list will be empty.

Scenario 1: If User is New and No Questions Answered Yet
If the user is newly registered and has not started the mock test yet, the output could look like this:

```json
{
    "id": 1,
    "user": 1,
    "questions_answered": [],
    "start_time": "2025-01-21T03:21:24.343121Z"
}
```
questions_answered is an empty list because no questions have been assigned yet.
Scenario 2: If the User Already Has Mock Test Data
If the user already has an existing mock test with answered questions, the response could be:

```json
{
    "id": 1,
    "user": 1,
    "questions_answered": [
        3, 5, 8
    ],
    "start_time": "2025-01-21T03:21:24.343121Z"
}
```
The questions_answered list would contain IDs of the questions that the user has already answered.
What You Should Expect Based on the Current Code:
If the user does not exist or is not provided: A response like this will be returned:
```json

{
    "detail": "User parameter is missing."
}
```
If no questions are available for the mock test (i.e., if the user has already answered all questions), the questions_answered list might be empty, and no new questions will be added.
Summary:
The output is a JSON object containing:

The mock test ID (id).
The user ID (user).
A list of questions_answered (which may contain question IDs assigned to the user).
The start_time timestamp when the mock test was created.
The list of questions_answered can be empty if no questions have been assigned yet or if the user has already answered all questions.
