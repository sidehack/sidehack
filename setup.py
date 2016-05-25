from setuptools import setup


setup(
    name="sidehack",
    version="0.1.5",
    author="Manas Hardas",
    author_email="manas@manashardas.com",
    description="Enterprise innovation intelligence",
    license="Proprietary",
    url="https://github.com/sidehack/sidehack.git",
    scripts = [],
    packages=[
        "sidehack",
        ],
    install_requires=[
        "pyramda",
        "numpy",
        "pandas",
        "flask",
        "MYSQL-python",
        "sqlalchemy"
    ],
    package_data={},
    tests_require=["nose"],
    zip_safe=False,
)
