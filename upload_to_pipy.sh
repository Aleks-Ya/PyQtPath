rm -rf dist
python -m build
python -m twine check dist/*
python -m twine upload dist/*
