import os

_datasets = os.path.normpath(os.path.join(os.getcwd(), '..', 'Datasets'))
if os.path.isdir(_datasets):
    os.chdir(_datasets)

print(f"Current working directory: {os.getcwd()}")