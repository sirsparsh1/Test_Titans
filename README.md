## Features Covered

- User Registration
- User Login & Logout
- Invalid Login Validation
- Product Search
- Product Details Verification
- Brand Filtering
- Category Browsing
- Add to Cart
- Remove from Cart
- Checkout Process
- Payment Validation
- Wishlist Management
- Product Review Submission
- Contact Us Form
- Newsletter Subscription
- Order Management
- API Product Validation



## Tech Stack

| Technology | Usage |
|------------|-------|
| Python | Programming Language |
| Selenium | UI Automation |
| Behave | BDD Framework |
| Pytest | Test Execution |
| Postman | API Testing |
| Newman | API Runner |
| Allure | Reporting |
| HTML Reports | Execution Reports |
| Git & GitHub | Version Control |



## Installation & Setup

### Clone Repository

```bash
git clone https://github.com/sirsparsh1/Test_Titans.git
```

### Navigate to Project

```bash
cd Capstone_Project
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

#### PowerShell

```bash
.\.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```



## Run Automation Tests

### Run Complete Framework

```bash
behave
```

### Run Specific Feature

```bash
behave features/user_login.feature
```

### Run Smoke Tests

```bash
behave --tags=smoke
```

### Run Regression Tests

```bash
behave --tags=regression
```




## Reports

### Generate HTML Report

```bash
behave -f behave_html_formatter:HTMLFormatter -o reports/report.html
```

### Generate Allure Results

```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-results features
```

### Open Allure Report

```bash
allure serve allure-results
```


## API Testing

### Run Postman Collection

```bash
newman run postman/AutomationExercise_API.postman_collection.json
```

### Generate Newman HTML Report

```bash
newman run postman/AutomationExercise_API.postman_collection.json -r html
```

## Framework Advantages

- Reusable Page Object Model
- Scalable Framework Design
- Easy Maintenance
- Supports UI + API Testing
- BDD Readable Scenarios
- Integrated Reporting
- Team Collaboration Support
