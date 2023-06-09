from generate_csv import generate_csv
from stock_analysis_gui import open_main_window
from data_analysis import perform_data_analysis

generate_csv()
analysis_results = perform_data_analysis()

if analysis_results is not None:
    open_main_window(analysis_results)
else:
    print("Exiting program due to missing data file.")
