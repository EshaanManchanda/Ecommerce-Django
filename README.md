# E-Commerce Project

## Overview

This is an e-commerce web application built with Django, featuring a product recommendation system optimized with Cython. The application includes basic e-commerce functionalities such as product display, user cart, and checkout process. The recommendation system is powered by a machine learning model that provides product recommendations based on user behavior and interactions.

## Features

- **Product Display:** View and browse a list of products with details.
- **User Cart:** Add products to the cart, view cart contents, and remove items.
- **Checkout Process:** Complete orders with user details and payment information.
- **Product Recommendations:** Get personalized product recommendations based on user interactions.
- **Performance Optimization:** Enhanced recommendation calculations using Cython.

## Installation

### Prerequisites

- Python 3.x
- Django
- Cython

### Setup

1. **Clone the Repository**

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Compile Cython Code**

   ```bash
   python setup.py build_ext --inplace
   ```

5. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

## Usage

- **Browse Products:** Navigate to `/products/` to view the list of products.
- **View Product Details:** Go to `/products/<product_id>/` to see details and recommendations.
- **Manage Cart:** Access the cart at `/cart/` to add or remove items.
- **Checkout:** Proceed to `/checkout/` to complete your purchase.

## Cython Optimization

Cython is used to optimize the cosine similarity calculation in the recommendation system. The `cython_modules/distance.pyx` file contains the optimized Cython code.

## Machine Learning Model

The recommendation system uses a machine learning model to provide product recommendations. The model is trained on product features and user interactions.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Django: A high-level Python web framework.
- Cython: A programming language that makes writing C extensions for Python as easy as Python itself.
- Scikit-learn: A machine learning library for Python.

