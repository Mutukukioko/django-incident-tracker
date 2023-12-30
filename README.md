# Security Incident Tracking API

A Django REST framework project for tracking and managing security incidents.

## Project Structure

- `incident_tracker/`: Django project directory
- `incidents/`: Django app directory containing models, views, and serializers
- ...

## Setup and Installation

1. **Create a virtual environment:**

   ```bash
   python3 -m venv myenv
   ```

2. **Activate the virtual environment:**

   - On Windows:
     ```bash
     myenv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source myenv/bin/activate
     ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

6. **Open your browser and navigate to [http://127.0.0.1:8000/api/incidents/](http://127.0.0.1:8000/api/incidents/) to view the API.**

## API Endpoints

- **GET /api/incidents/**: Retrieve a list of all security incidents.
- **POST /api/incidents/**: Create a new security incident.
- **GET /api/incidents/{id}/**: Retrieve details of a specific security incident.
- **PUT /api/incidents/{id}/**: Update details of a specific security incident.
- **DELETE /api/incidents/{id}/**: Delete a specific security incident.

## Dependencies

- Django: 3.2.0
- Django REST Framework: 3.12.2
- ...

## Contribution Guidelines

We welcome contributions! If you'd like to contribute to this project, please follow our [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact

For questions or collaboration, feel free to reach out:

- Email: imutkupc@gmail.com
- LinkedIn: [www.linkedin.com/in/harrisonmutuku](www.linkedin.com/in/harrisonmutuku)


