# Gene Ontology Analysis System

## Overview
This project is a Gene Ontology (GO) Analysis System that allows users to analyze biological data using GO terms and annotations. It provides multiple analytical tools through a web-based interface built with Flask.

## Features
- Statistics of GO terms and annotations
- GO Term search
- Gene search
- Similarity analysis (Jaccard, Cosine, etc.)
- Neighborhood analysis of GO terms
- Upload OBO and GAF files

## Technologies Used
- Python
- Flask
- HTML (Jinja Templates)
- Pandas / NumPy

## Project Structure
gene-ontology-analysis-system/
│
├── app.py
├── src/
├── templates/
├── tests/
├── README.md
├── .gitignore

## How to Run the Project

1. Install required libraries:
pip install flask pandas numpy

2. Run the application:
python app.py

3. Open in browser:
http://localhost:8000

## Usage Instructions
1. Open the homepage
2. Use available features:
   - Statistics
   - Similarity Analysis
   - Gene Search
   - GO Term Search
   - Neighborhood Analysis
3. Upload your own:
   - .obo file
   - .gaf or .gaf.gz file

## Important Notes
- Large data files are NOT included in the repository
- Users should upload their own datasets using the Upload page
- .gitignore is used to exclude unnecessary large files

## Author
Pegah Mohebbi
