# from distutils.core import setup

# setup(
#     name = 'VGo',
#     packages = ['pyttsx3'],
#     version = 'version number',  # Ideally should be same as your GitHub release tag varsion
#     description = 'VGo',
#     author = 'VGo developer team',
#     author_email = 'dghan98@gmail.com',
#     url = 'https://github.com/giahandiep/VGo',
#     download_url = 'download link you saved',
#     keywords = ['tag1', 'tag2'],
#     classifiers = [],
# )

name: Python package

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [2.7, 3.5, 3.6, 3.7, 3.8]

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest
      run: |
        pytest
        pip install git+https://github.com/MartinoMensio/spacy-universal-sentence-encoder-tfhub.git # spacy 