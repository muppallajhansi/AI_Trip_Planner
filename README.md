# Environment Setup

If you have any Conda environment activated, deactivate it using:

```bash
conda deactivate
```

Check the Python versions available on your system:

```bash
uv python list
```

Install Python 3.12.12 (if it is not already installed):

```bash
uv python install cpython-3.12.12-windows-x86_64-none
```

Create a virtual environment using Python 3.12.12:

```bash
uv venv env --python cpython-3.12.12-windows-x86_64-none
```

Activate the virtual environment:

```bash
C:\Users\19459\AI_Trip_Planner\env\Scripts\activate.bat
```

Install a package (example):

```bash
uv pip install langchain
```


