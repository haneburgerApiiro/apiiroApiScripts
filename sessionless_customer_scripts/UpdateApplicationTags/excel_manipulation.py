#!/usr/bin/env python3
import pandas as pd
from colorama import Fore, Style, init

def remove_duplicates(input_file, output_file):
    init(autoreset=True)
    
    # Reading the Excel file
    df = pd.read_excel(input_file)
    
    seen_ids = set()
    rows_to_keep = []
    removed_count = 0
    
    for _, row in df.iterrows():
        row_id = row["Id"] #Change this ID to the column name you want to check for duplicates
        if row_id not in seen_ids:
            seen_ids.add(row_id)
            print(row.to_dict())
            rows_to_keep.append(row)
        else:
            print(Fore.RED + str(row.to_dict())) 
            removed_count += 1
    
    kept_count = len(rows_to_keep)
    
    # Saving DataFrame without duplicates
    print(Fore.GREEN + f"\nTotal records processed: {len(df)}")
    df_no_dupes = pd.DataFrame(rows_to_keep)
    df_no_dupes.to_excel(output_file, index=False)
    
    # Summary output
    print(Fore.YELLOW + f"\nUnique records: {kept_count}")
    print(Fore.YELLOW + f"Non-unique records deleted: {removed_count}")
    print(Style.RESET_ALL + f"\nDuplicates removed. Saved as '{output_file}'.")

def keep_first_rows(file_path: str, num_rows: int, output_file: str = "output.xlsx"):
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Keep the first num_rows rows
    df_limited = df.head(num_rows)
    
    # Save to a new file
    df_limited.to_excel(output_file, index=False)
    print(f"Saved first {num_rows} rows to '{output_file}'.")

def main():
    keep_first_rows(file_path="outdated/Inventory_Primary.xlsx", num_rows=10, output_file="Inventory_first_10_rows.xlsx")


if __name__ == "__main__":
    main()