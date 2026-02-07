# Publishing Guide for Django NG Locations

This guide explains how to publish the `django-ng-locations` package to PyPI and GitHub.

## Prerequisites

1. **GitHub Account**: Create an account at https://github.com
2. **PyPI Account**: Create an account at https://pypi.org
3. **Git**: Install Git on your system
4. **Python Build Tools**: Install required tools

```bash
pip install build twine
```

## Step 1: Prepare the Package

### Update Package Information

1. Edit `setup.py` and `pyproject.toml`:
   - Replace `"Your Name"` with your actual name
   - Replace `"your.email@example.com"` with your email
   - Update the GitHub URL with your username

2. Edit `README.md`:
   - Update author information
   - Update repository URLs

3. Review `CHANGELOG.md` and update version information

## Step 2: Create GitHub Repository

### Initialize Git Repository

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Django NG Locations package"
```

### Create Repository on GitHub

1. Go to https://github.com/new
2. Repository name: `django-ng-locations`
3. Description: "A comprehensive Django package for Nigerian geographic data"
4. Choose Public
5. Don't initialize with README (we already have one)
6. Click "Create repository"

### Push to GitHub

```bash
# Add remote
git remote add origin https://github.com/YOUR_USERNAME/django-ng-locations.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Build the Package

```bash
# Clean previous builds
rm -rf build/ dist/ *.egg-info

# Build the package
python -m build
```

This creates:
- `dist/django-ng-locations-0.1.0.tar.gz` (source distribution)
- `dist/django_ng_locations-0.1.0-py3-none-any.whl` (wheel distribution)

## Step 4: Test the Package Locally

```bash
# Install in development mode
pip install -e .

# Or install from the built wheel
pip install dist/django_ng_locations-0.1.0-py3-none-any.whl
```

## Step 5: Upload to PyPI

### Test on TestPyPI First (Recommended)

1. Create account at https://test.pypi.org
2. Upload to TestPyPI:

```bash
python -m twine upload --repository testpypi dist/*
```

3. Test installation:

```bash
pip install --index-url https://test.pypi.org/simple/ django-ng-locations
```

### Upload to PyPI

```bash
# Upload to PyPI
python -m twine upload dist/*
```

You'll be prompted for your PyPI username and password.

### Using API Tokens (Recommended)

1. Go to https://pypi.org/manage/account/token/
2. Create a new API token
3. Use `__token__` as username and the token as password

Or configure in `~/.pypirc`:

```ini
[pypi]
username = __token__
password = pypi-YOUR-API-TOKEN-HERE
```

## Step 6: Create GitHub Release

1. Go to your repository on GitHub
2. Click "Releases" → "Create a new release"
3. Tag version: `v0.1.0`
4. Release title: `v0.1.0 - Initial Release`
5. Description: Copy from CHANGELOG.md
6. Attach the distribution files from `dist/`
7. Click "Publish release"

## Step 7: Verify Installation

Test that users can install your package:

```bash
pip install django-ng-locations
```

## Updating the Package

When you make changes and want to release a new version:

1. Update version in `setup.py` and `pyproject.toml`
2. Update `CHANGELOG.md`
3. Commit changes
4. Create a git tag:

```bash
git tag -a v0.2.0 -m "Version 0.2.0"
git push origin v0.2.0
```

5. Build and upload:

```bash
rm -rf build/ dist/ *.egg-info
python -m build
python -m twine upload dist/*
```

6. Create GitHub release

## Package Structure

Your final package structure should look like:

```
django-ng-locations/
├── django_ng_locations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── utils.py
│   ├── fixtures/
│   │   ├── __init__.py
│   │   └── nigeria_data.py
│   ├── management/
│   │   ├── __init__.py
│   │   └── commands/
│   │       ├── __init__.py
│   │       └── load_ng_locations.py
│   └── migrations/
│       └── __init__.py
├── setup.py
├── pyproject.toml
├── MANIFEST.in
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── requirements.txt
├── requirements-dev.txt
└── .gitignore
```

## Troubleshooting

### Package Name Already Exists

If `django-ng-locations` is taken, try:
- `django-nigeria-locations`
- `django-ng-geo`
- `ng-locations`

### Import Errors

Make sure `__init__.py` files exist in all package directories.

### Missing Files in Distribution

Check `MANIFEST.in` and `setup.py` package_data configuration.

## Resources

- PyPI: https://pypi.org
- Python Packaging Guide: https://packaging.python.org
- Django Packages: https://djangopackages.org
- Twine Documentation: https://twine.readthedocs.io

## Support

For issues, create a GitHub issue at:
https://github.com/YOUR_USERNAME/django-ng-locations/issues

