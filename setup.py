from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="django-ng-locations",
    version="0.1.0",
    author="Olaniyan Adewale Hafeez",
    author_email="support@techwareinnovation.com",
    description="A comprehensive Django package for Nigerian geographic data (zones, states, LGAs) with models for cities, wards, and postal codes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abdulhafeez1432/django-ng-locations",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Framework :: Django",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Framework :: Django :: 6.0",
    ],
    python_requires=">=3.8",
    install_requires=[
        "Django>=4.0",
    ],
    include_package_data=True,
    package_data={
        "django_ng_locations": [
            "fixtures/*.json",
            "management/commands/*.py",
        ],
    },
    keywords="django nigeria locations states lga zones cities wards postal-codes",
    project_urls={
        "Bug Reports": "https://github.com/abdulhafeez1432/django-ng-locations/issues",
        "Source": "https://github.com/abdulhafeez1432/django-ng-locations",
    },
)

