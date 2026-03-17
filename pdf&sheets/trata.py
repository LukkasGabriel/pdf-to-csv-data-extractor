# Import the Tabula library used to extract tables from PDF files
import tabula

# Import pandas for data manipulation and analysis
import pandas as pd


# Read tables from the PDF file
# pages="all" -> reads tables from all pages
# multiple_tables=True -> allows Tabula to extract multiple tables per page
pdf = tabula.read_pdf("australian_ecommerce.pdf", pages="all", multiple_tables=True)


# Tabula returns a LIST of DataFrames (one for each detected table)
# pd.concat() merges all DataFrames into a single DataFrame
df = pd.concat(pdf)

print(df.head(50))

# Export the final DataFrame to a CSV file
# index=False -> prevents pandas from writing the row index as a column
# df.to_csv("new_file.csv", index=False)