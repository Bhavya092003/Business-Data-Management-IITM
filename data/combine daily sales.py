import os
import glob
import pandas as pd

def combine_monthly_excel_files(input_folder, output_folder, output_filename="monthly_combined.xlsx", skip_dates=None):
    if skip_dates is None:
        skip_dates = []

    # Match all .xlsx files in the folder with YYYY-MM-DD format
    pattern = os.path.join(input_folder, "2024-11-??.xlsx")
    file_list = sorted(glob.glob(pattern))

    combined_data = []

    for file_path in file_list:
        filename = os.path.basename(file_path)
        file_date = filename.split(".")[0]  # Extract date part

        if file_date in skip_dates:
            print(f"Skipping: {filename}")
            continue

        try:
            df = pd.read_excel(file_path)
            df["Date"] = pd.to_datetime(file_date)
            combined_data.append(df)
            print(f"Processed: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    if combined_data:
        monthly_df = pd.concat(combined_data, ignore_index=True)
        output_path = os.path.join(output_folder, output_filename)
        monthly_df.to_excel(output_path, index=False)
        print(f"\nCombined file saved to: {output_path}")
    else:
        print("\nNo data combined. Check filenames or folder path.")

if __name__ == "__main__":
    input_folder = r"E:\daily sales"
    output_folder = r"E:\data"
    skip = []  
    combine_monthly_excel_files(input_folder, output_folder, skip_dates=skip)
