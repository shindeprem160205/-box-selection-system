# AI Usage

## AI Tools Used

- ChatGPT

## 1. Basic Project Structure

    used AI tools like ChatGPT because they help me understand better project structures. I usually ask ChatGPT for an overview of a project or technology to get a better understanding of the task. However, I always cross-check the information before using it in my projects.

### Prompt 1

> This is a task allocated to me. I have been asked to build a Django REST API project for a recommendation-type system. It has classes/models such as Order, Product, and Box. What would be the basic structure of the project?   

### Prompt 2 — Box Selection Logic

> How should the box-selection and recommendation logic be designed

### Prompt 3 — Serializers

> i have created product, box, order, and orderitem models in my django project. how should i create serializer for these models using django rest framework? i also need validation for fields like dimensions, weight, and quantity. please provide the serialiZer code and explain how it works.

### Prompt 4 — README Formatting

> i also used chatgpt for readme formatting and making readme more cleaner

## 2. Output I Accepted

    I accepted the basic Django project structure suggested by ChatGPT.
    It helped me understand how to separate the project into different apps such as
    Products, Boxes, and Orders.

    And Output was same as expected So I accepted it because structre was clear.

    And most of the output was not directly used as code and even If I reqired I used the code and modified It accordingly and in feww instances I not changed code as it working perfectly.

    Most of gpt code was used during validation and searlizing by undersatnding its use cases.

## 3. Output I Rejected or Modified

    The field validation in DRF serializers was tricky for me, so I used ChatGPT to understand and implement it. I accepted the suggested code because it was working correctly and I did not face any issues with it.

    I did not blindly accept all the outputs. I cross-checked the code and properly implemented and tested it before accepting it. I also did not reject the serializer code because it worked correctly and did not cause any further issues during the project.

## 4. Mistakes Made by AI

    ChatGPT initially assumed a different relationship for the Order model, using a ManyToMany relationship with Product. My actual project uses a separate OrderItem model with Order, Product, and quantity.

    I checked the output against my actual project structure and did not use that part directly. I kept the existing Order and OrderItem structure and adjusted the explanation accordingly.

    Because of this, I do not blindly trust AI-generated code. I always cross-check the output, understand how it works, and test it before using it in a project.
## 5. How I Verified the Final Code

    I verified the AI-generated suggestions by implementing them in my Django project and testing them myself.

    I used the following commands during development and final verification:

    ```bash
    python manage.py check
    python manage.py makemigrations
    python manage.py makemigrations --check
    python manage.py migrate
    python manage.py test
    python manage.py runserver
