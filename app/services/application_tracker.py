import sqlite3


DATABASE = "app/services/careerpilot.db"

VALID_STATUSES = [
    "Saved",
    "Applied",
    "Interview",
    "Selected",
    "Rejected"
]


def get_connection():
    return sqlite3.connect(DATABASE)


def initialize_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            application_id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            company TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_application(
    role: str,
    company: str,
    status: str = "Saved"
) -> dict:

    role = role.strip()
    company = company.strip()
    status = status.strip()

    if not role:
        return {
            "success": False,
            "message": "Please provide an internship role."
        }

    if not company:
        return {
            "success": False,
            "message": "Please provide a company name."
        }

    if status not in VALID_STATUSES:
        return {
            "success": False,
            "message": (
                f"Invalid status. Choose one of: "
                f"{', '.join(VALID_STATUSES)}"
            )
        }

    connection = get_connection()

    cursor = connection.execute(
        """
        INSERT INTO applications (role, company, status)
        VALUES (?, ?, ?)
        """,
        (role, company, status)
    )

    application_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return {
        "success": True,
        "message": "Application added successfully.",
        "application": {
            "application_id": application_id,
            "role": role,
            "company": company,
            "status": status
        }
    }


def get_applications() -> dict:

    connection = get_connection()

    rows = connection.execute(
        """
        SELECT application_id, role, company, status
        FROM applications
        ORDER BY application_id
        """
    ).fetchall()

    connection.close()

    applications = [
        {
            "application_id": row[0],
            "role": row[1],
            "company": row[2],
            "status": row[3]
        }
        for row in rows
    ]

    return {
        "success": True,
        "total_applications": len(applications),
        "applications": applications
    }


def update_application_status(
    application_id: int,
    status: str
) -> dict:

    status = status.strip()

    if status not in VALID_STATUSES:
        return {
            "success": False,
            "message": (
                f"Invalid status. Choose one of: "
                f"{', '.join(VALID_STATUSES)}"
            )
        }

    connection = get_connection()

    cursor = connection.execute(
        """
        UPDATE applications
        SET status = ?
        WHERE application_id = ?
        """,
        (status, application_id)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()

        return {
            "success": False,
            "message": f"Application with ID {application_id} was not found."
        }

    row = connection.execute(
        """
        SELECT application_id, role, company, status
        FROM applications
        WHERE application_id = ?
        """,
        (application_id,)
    ).fetchone()

    connection.close()

    return {
        "success": True,
        "message": "Application status updated successfully.",
        "application": {
            "application_id": row[0],
            "role": row[1],
            "company": row[2],
            "status": row[3]
        }
    }


initialize_database()