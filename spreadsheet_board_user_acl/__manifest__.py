{
    "name": "Spreadsheet Board User ACL",
    "summary": """
        Restricted access to spreadsheet dashboards app.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://www.mint-system.ch",
    "category": "Technical",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["spreadsheet_dashboard"],
    "data": ["security/security.xml", "views/menu.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
