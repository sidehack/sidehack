from setuptools import setup


setup(
    name="sidehack",
    version="0.0.1",
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
        "django"
    ],
    package_data={},
    tests_require=["nose"],
    zip_safe=False,
)
