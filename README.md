# Fubuki Project Template

This is a project template for building web applications using the [Fubuki](https://github.com/fubuki-dev/fubuki) ASGI framework.

## Features
- **Fubuki Framework**: This template uses the Fubuki ASGI framework for building the web application.
- **Routing and Controllers**: The template includes an example of defining routes and controllers using Fubuki's features.
- **Templates**: The template includes an example of using HTML templates.

## Getting Started
### With PDM
PDM 2.8.0 or later makes it easy to use this template.

Simply execute the following command: 
```
pdm init https://github.com/fubuki-dev/template
```
### Without PDM
1. **Create a new repository from this template**: Click the "Use this template" button on the top right of this page to create a new repository based on this template.

2. **Clone the repository**: Clone the newly created repository to your local machine.

```bash
git clone https://github.com/your-username/your-project.git
cd your-project
```

3. **Install dependencies**: Install the project dependencies using pip or your preferred package manager.

```bash
pip install -r requirements.txt
```

4. **Run the application**: Run the application using the provided CLI command.

```bash
python main.py
```

This will start the Fubuki application on `http://localhost:8000`.

5. **Explore the project structure**: The project structure is as follows:

```
your-project/
├── app/
│   ├── __init__.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── user_controller.py
│   │   └── home_controller.py
│   └── routes.py
├── templates/
│   └── index.html
├── app.py
└── main.py
```

- The `app` directory contains the main application code, including controllers, middlewares, templates, and static files.
- The `app.py` file is the main entry point for the Fubuki application.
- The `main.py` file is used to start the application.

6. **Customize the application**: Modify the existing code or add new features to your web application. Refer to the [Fubuki documentation](https://fubuki-dev.github.io/docs) for more information on using the framework.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request. 