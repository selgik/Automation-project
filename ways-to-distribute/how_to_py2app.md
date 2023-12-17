# How to convert python script to app using py2app
## Documentation [Link](https://py2app.readthedocs.io/en/latest/command-line.html)
### 1. Install py2app with pip
- On the terminal, type: pip3 install py2app

### 2. Create setup.py file
- I manually created below setup.py file to configure py2app.
- setup.py file should be in the same directory where my script is.
```python
from setuptools import setup

setup(
    app=['my_script.py'],
    setup_requires=['py2app'],
)
```

### 3. Run setup.py file
- On the terminal, type: python3 -m setup.py py2app
- As a result of this conversion, (1) dist folder and (2) build folder will be generated
  - Under the dist folder, you can check executable app 
