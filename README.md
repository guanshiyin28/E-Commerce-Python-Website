# E-Commerce Python Website

This repository aims to provide a starting point for developing a Python-based marketplace web application.

<hr><br>

## Purpose of This Repository

This repository serves as a foundational framework for developing a Python-based marketplace web application, encompassing core features such as user registration and authentication, product listing and management, basic search functionality, and a user-friendly interface, providing a robust starting point for developers seeking to build a dynamic and scalable online marketplace platform.

<hr><br>

## Demonstration

Here is a demonstration of the `add_product` function from `app.py`:

```python
def add_product(name, description, price):
    product = {
        'name': name,
        'description': description,
        'price': price
    }
    # Code to add the product to the database
    return product

# Example usage
new_product = add_product('Sample Product', 'This is a sample product.', 19.99)
print(new_product)
```

<hr><br>

## Features

- User registration and authentication
- Product listing and management
- Basic search functionality
- User-friendly interface
- Responsive design

<hr><br>

## Technologies Used

- Python
- Flask
- SQLite
- HTML/CSS
- JavaScript

<hr><br>

## Project Setup

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python installed on your machine
- pip (Python package installer)

### Steps to Run

1. Install Python
2. Install & upgrade pip

```bash
python -m ensurepip --upgrade
python get-pip.py
python -m pip install --upgrade pip
```

3. Clone this Repository

```bash
git clone https://github.com/guanshiyin28/E-Commerce-Python-Website.git
```

4. Direct to the directory

```bash
cd E-Commerce-Python-Website
```

5. Install requirements.txt

```bash
pip install -r requirements.txt
```

6. Run with Python and see through the localhost

```bash
python app.py
```

<hr><br>

## License

This project is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) file for details.

<hr><br>

<div align="center">
   <a href="https://www.instagram.com/guanshiyin_/">
      <img src="https://capsule-render.vercel.app/api?type=waving&height=200&color=100:393E46,20:F7F7F7&section=footer&reversal=false&textBg=false&fontAlignY=50&descAlign=48&descAlignY=59"/>
   </a>
</div>
