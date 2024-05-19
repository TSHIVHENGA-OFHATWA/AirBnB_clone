1. Description of the project
     AirBnB Clone Command Interpreter

    
    This project is a command-line interpreter (CLI) designed to manage objects within an AirBnB clone ecosystem. 
    The CLI allows users to perform various operations on objects, including creating new instances,
    retrieving existing instances, performing operations like counting and computing statistics, updating attributes,
     and destroying objects.

    # Features

    - BaseModel Class: A parent class handling initialization, serialization, and deserialization of instances.
    - Serialization/Deserialization Flow: Converts instances to dictionaries, JSON strings, and files, and vice versa.
    - AirBnB Classes: Classes representing various components of the AirBnB ecosystem, such as User, State, City, Place, etc.
    - Storage Engine: Implements a basic storage engine, initially as file storage, responsible for storing and retrieving instances of objects.
    - Unit Tests: Includes unit tests to validate the functionality of all classes and the storage engine.

2. Description of the command interpreter:
    The command interpreter (console.py) is a crucial component of the AirBnB clone project. 
    It allows users to create, manage, and manipulate various objects like BaseModel, User,
    State, City, Place, Amenity, and Review.
    Through this interpreter, users can perform CRUD operations (Create, Read, Update, Delete) on the objects.

  2.1 How to start it
      ./console.py
      
      python3 console.py

  2.2 How to use it
      Once the interpreter is running, you will see a prompt (hbnb) indicating that the interpreter is ready to accept commands. 

      Here are the commands you can use:

       quit or EOF: Exit the command interpreter.

       create <class_name>: Create a new instance of a class and print its id.

       show <class_name> <id>: Show the string representation of an instance based on the class name and id.

       destroy <class_name> <id>: Delete an instance based on the class name and id.

       all [<class_name>]: Print all string representations of all instances, or all instances of a specific class.

       update <class_name> <id> <attribute_name> <attribute_value>: 
           Update an instance based on the class name and id by adding or updating an attribute.

  2.3 examples

       (hbnb) create BaseModel
       d8f33f1e-7c2d-4c3c-9a3b-9a0f4c1d1f7a

       (hbnb) show BaseModel d8f33f1e-7c2d-4c3c-9a3b-9a0f4c1d1f7a
       [BaseModel] (d8f33f1e-7c2d-4c3c-9a3b-9a0f4c1d1f7a) {'id': 'd8f33f1e-7c2d-4c3c-9a3b-9a0f4c1d1f7a', 
                    'created_at': '2023-05-01T12:00:00.000000', 'updated_at': '2023-05-01T12:00:00.000000'}
        
       (hbnb) destroy BaseModel d8f33f1e-7c2d-4c3c-9a3b-9a0f4c1d1f7a
