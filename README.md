# Online-Beauty-Store

## Description

The Cosmetics Online Store Database is a comprehensive solution for managing various aspects of an online cosmetics store. It facilitates efficient handling of employee data, customer information, sales transactions, product inventory, and category management. The database employs a relational model with well-defined tables and establishes relationships between entities to ensure data integrity and seamless operations.

## Database Details

The database was created using Microsoft SQL Server 2014, leveraging its robust features and capabilities for data management and security. The codebase is connected to this SQL Server database, enabling seamless integration and interaction with the stored data.


## Features

- **Employee Management:** Stores employee details including their department affiliation, allowing effective management of staff resources.
- **Customer Database:** Manages customer information such as contact details, addresses, and purchase history for personalized services and targeted marketing.
- **Sales Transactions:** Records sales transactions, linking clients with purchased products and the employee who processed the transaction for accurate reporting and analysis.
- **Product Inventory:** Maintains product inventory with details like product name, price, and category, enabling efficient stock management and product tracking.
- **Category Management:** Organizes products into categories, facilitating browsing and navigation for customers and efficient catalog management for administrators.
- **User Authentication:** Implements user authentication to restrict access to authorized personnel, ensuring data security and confidentiality.
- **Graphical User Interface (GUI):** Provides a user-friendly interface developed in Python with graphical components for easy navigation and interaction with the database.


## Database Schema

The database comprises the following tables:

- **Employee:** Stores employee information, including department affiliation and salary details. Operations: Add, Delete
- **Department:** Contains details about different departments within the organization, including the manager responsible for each department. Operations: Add, Delete
- **Client:** Stores customer data, including personal information and address details. Operations: Add, Delete
- **Receipt:** Records sales transactions made by clients, linking clients, employees, and purchase details. Operations: Add, Delete
- **Product:** Contains information about the products available in the store, including product name, price, and category. Operations: Add, Delete
- **Category:** Stores the categories to which products belong, facilitating product organization and navigation. Operations: Add, Delete
- **Order:** Resolves the many-to-many relationship between receipts and products, recording product quantities purchased in each transaction. Operations: Add, Delete

## Implementation Details

- **Database Design:** Follows normalized database design principles to minimize redundancy and ensure data consistency.
- **Data Validation:** Implements constraints and validations to enforce data integrity and prevent data anomalies.
- **User Interface:** Develops a graphical user interface (GUI) using Python and suitable libraries for seamless interaction with the database.
- **User Authentication:** Implements user authentication mechanisms to control access and ensure data security.
- **Data Manipulation:** Supports CRUD operations (Create, Read, Update, Delete) to manage database records efficiently.
- **Query Execution:** Enables execution of predefined queries and supports custom queries for flexible data retrieval and analysis.

## Usage

1. **Login:** Authenticate with valid credentials to access the database interface.
2. **Navigation:** Use the graphical interface to navigate through different tables and functionalities.
3. **Data Modification:** Perform CRUD operations to add, update, or delete records as necessary.
4. **Query Execution:** Execute predefined queries or create custom queries to retrieve specific information from the database.

## Future Enhancements

- Integration with external systems for enhanced functionality.
- Implementation of advanced analytics and reporting features.
- Expansion of user roles and permissions for finer control over data access.
- Integration of additional authentication mechanisms for enhanced security.
