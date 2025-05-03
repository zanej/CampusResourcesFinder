# CampusResourcesFinder
Campus Resource Finder is a full-stack interactive web application built to help Texas A&M University students quickly locate and navigate to essential campus resources. From food pantries and emergency aid to dining halls, libraries, gyms, and academic buildings, this tool makes finding support services fast, easy, and stigma-free.

The app features a filterable, searchable map interface powered by Leaflet.js, integrated with real-time directions using Leaflet Routing Machine. Students can get walking, biking, or driving directions from their current location to any selected resource. The database includes multilingual support for English and Spanish, with a dynamic language switcher that reloads listings accordingly.

Technologies used include Flask for the Python backend, SQLite for the data layer, and HTML, CSS, and vanilla JavaScript for the frontend. The project is fully responsive for both desktop and mobile users.

To get started, clone the repository:
git clone https://github.com/your-username/campus-resource-finder.git
cd campus-resource-finder

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate


Install dependencies:
pip install flask
Initialize the database:

python init_db.py

sql
Copy
Edit

Then start the server:

python app.py

Once running, open your browser to http://127.0.0.1:5000 to access the application.

Planned improvements include integration with Texas A&M's live bus system, downloadable PDF resource lists, favorite location saving, an admin dashboard for entry management, and broader language and accessibility support.
