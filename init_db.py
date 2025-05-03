import sqlite3

conn = sqlite3.connect('resources.db')
c = conn.cursor()

# Create the table with UNIQUE constraint on (name, address)
c.execute('''
CREATE TABLE IF NOT EXISTS resources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    category TEXT,
    latitude REAL,
    longitude REAL,
    address TEXT,
    contact TEXT,
    UNIQUE(name, address)
)
''')

resources = [
    # Assistance
    ('Aggie Food Pantry', 'Groceries for students in need', 'Food', 30.6178, -96.3365, 'Student Services Building', 'food@tamu.edu'),
    ('Student Emergency Fund', 'Crisis housing and bills support', 'Emergency Aid', 30.6155, -96.3377, 'Koldus', 'aid@tamu.edu'),

    # Support
    ('CAPS', 'Mental health support', 'Counseling', 30.617, -96.3369, 'White Creek', 'caps@tamu.edu'),
    ('ASC', 'Tutoring and workshops', 'Tutoring', 30.619, -96.3401, 'Zachry', 'success@tamu.edu'),

    # Dining Halls
    ('Sbisa Dining Hall', 'Buffet-style dining on Northside', 'Dining Hall', 30.619007, -96.340331, 'Sbisa Hall', 'dining@tamu.edu'),
    ('The Commons Dining Hall', 'Southside dining with diverse options', 'Dining Hall', 30.611315, -96.345122, 'The Commons', 'commons@tamu.edu'),
    ('Duncan Dining Hall', 'Buffet near Corps dorms', 'Dining Hall', 30.613114, -96.342855, 'Duncan Hall', 'duncan@tamu.edu'),

    # Gyms
    ('Student Recreation Center', 'Weights, cardio, pool, courts', 'Gym', 30.610267, -96.340962, 'Rec Center', 'recsports@tamu.edu'),
    ('Penberthy Rec Complex', 'Outdoor sports fields and facilities', 'Gym', 30.605472, -96.351179, 'Penberthy', 'penberthy@tamu.edu'),
    ('Southside Rec Center', 'Fitness center near Commons dorms', 'Gym', 30.610512, -96.344829, 'Southside Rec', 'southrec@tamu.edu'),

    # Libraries
    ('Evans Library', 'Main library with large study areas', 'Library', 30.618913, -96.338439, 'Evans Library, College Station, TX', 'evans@library.tamu.edu'),
    ('Medical Sciences Library', 'Health & medical specialization', 'Library', 30.612482, -96.342229, 'Med Sci Library, TAMU', 'msl@library.tamu.edu'),
    ('Cushing Library', 'Rare books and archives', 'Library', 30.618031, -96.341761, 'Cushing Memorial Library, TAMU', 'cushing@library.tamu.edu'),

    # Academic Buildings
    ('Zachry Engineering Complex', 'Main engineering building with labs and lecture halls', 'Academic Building', 30.619637, -96.338986, 'ZACH', 'zach@tamu.edu'),
    ('Blocker Building', 'Math, stats, and languages departments', 'Academic Building', 30.617403, -96.340932, 'Blocker', 'blocker@tamu.edu'),
    ('Academic Building', 'Classic A&M landmark with classrooms', 'Academic Building', 30.615276, -96.341610, 'Academic Plaza', 'acad@tamu.edu'),

    # Bus Stops
    ('MSC Bus Stop', 'Main transfer hub near Memorial Student Center', 'Bus Stop', 30.612677, -96.341196, 'MSC', 'transport@tamu.edu'),
    ('Zachry Bus Stop', 'Engineering and central campus access', 'Bus Stop', 30.619837, -96.338888, 'ZACH', 'transport@tamu.edu'),

    # Parking
    ('University Center Garage (UCG)', 'Visitor and student parking', 'Parking', 30.613766, -96.342144, 'UCG', 'parking@tamu.edu'),
    ('West Campus Garage (WCG)', 'Located near the Rec', 'Parking', 30.609775, -96.343865, 'WCG', 'parking@tamu.edu'),

    # Housing
    ('Hullabaloo Hall', 'Northside dorm with private bathrooms', 'Housing', 30.619927, -96.340526, 'Hullabaloo', 'housing@tamu.edu'),
    ('White Creek Apartments', 'Upperclassman apartments', 'Housing', 30.608127, -96.359707, 'White Creek', 'housing@tamu.edu'),

    # Safety
    ('University Police Department', 'Campus safety and emergency response', 'Safety', 30.613395, -96.343400, 'UPD HQ', 'upd@tamu.edu'),
    ('Blue Light Station (ZACH)', 'Emergency call station near Zachry', 'Safety', 30.619580, -96.339400, 'Zachry', 'none')
]

# Insert data, ignoring duplicates based on UNIQUE(name, address)
c.executemany('''
    INSERT OR IGNORE INTO resources (name, description, category, latitude, longitude, address, contact)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', resources)

conn.commit()
conn.close()
print("✅ resources.db created with full TAMU dataset (no duplicates).")
