# Django Mobile Inventory Project

This project is a Django-based mobile inventory system, designed for managing brands and mobile phones. The project includes CRUD operations for mobile phone and brand data, as well as features for searching and reporting.

## Features

- **CRUD Operations**: The system allows for Create, Read, Update, and Delete operations for both Phone and Brand models, giving flexibility in managing inventory data.
- **Custom User Model**: A minimally customized Django user model has been implemented to enhance user management and provide additional security.
- **Permissions and Access Control**: Permission levels and access control have been added. Login is required for certain views, ensuring that only authorized users can access sensitive data.
- **Search Functionality**: Users can search for phones by brand name or model, with results displayed dynamically.
- **Reports**: A specialized view generates reports where the brand nationality matches the country of manufacture, giving insight into brand localization.

## Project Setup

### Prerequisites
- Python 3.10
- PostgreSQL 13

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mobile-inventory.git
   cd mobile-inventory
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

### Running the Project
- Once the project is running, access it at `http://localhost:8000`.
- The admin panel can be accessed at `http://localhost:8000/adm-pnl` for managing users and data.

## API Endpoints

- **Search Phones**: `/api/search/` - Allows users to search for phones by brand or model name.
- **Nationality Equal Country Report**: `/api/report/` - Generates a report of phones where the brand nationality matches the country of manufacture.
- **CRUD Operations**: CRUD operations are available for both Phone and Brand models through the Django admin interface or through custom views.

## Models

- **Phone**: Represents mobile phones with fields such as `brand`, `model`, `price`, `color`, `screen_size`, `status`, and `country_of_manufacture`.
- **Brand**: Represents a brand with fields such as `name` and `nationality` to provide flexibility for managing multiple brands.

## Access Control

- **Custom User Model**: The project uses a minimally customized version of Django's default user model to support extended authentication needs.
- **Permissions**: Access control has been implemented to restrict certain views to logged-in users. Permissions are used to protect sensitive operations and data.

## Future Improvements
- Add unit tests to further validate the system.
- Implement more advanced filtering and reporting features.
- Expand user roles and permissions for finer access control.


