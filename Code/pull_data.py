import os
import pandas as pd
import copernicusmarine

subset_dict = {
    'dataset_id': 'cmems_obs-oc_glo_bgc-plankton_my_l3-multi-4km_P1D',
    'minimum_longitude': 38.0,
    'maximum_longitude': 48.0,
    'minimum_latitude': -6,
    'maximum_latitude': 0,
    'start_datetime': '1997/9/5',
    'end_datetime': '2025/9/28',
    'output_directory':r'C:\Users\geogdtsci_312\CDEdirectory\geog-312\Chlorophyll_a_levels_within_Kenya_s_EEZ\data',
    'output_filename': 'kenya_coast_ocean_color_1997_2025',
    'variables': ['CHL']
}
 

start = pd.Timestamp(subset_dict['start_datetime'])
end = pd.Timestamp(subset_dict['end_datetime'])
print(f"start: {start} \nend: {end}")

for year_begin in pd.date_range(start, end, periods=29):
    year_end = (year_begin + pd.DateOffset(years=1))
    

    filename = "chl_data_{0}_{1}.nc".format(str(year_begin.date()), str(year_end.date()))
    print(f"{year_begin.date()} to {year_end.date()}")
    copernicusmarine.subset(dataset_id=subset_dict['dataset_id'],
                        minimum_longitude=subset_dict['minimum_longitude'],
                        maximum_longitude=subset_dict['maximum_longitude'],
                        minimum_latitude=subset_dict['minimum_latitude'],
                        maximum_latitude=subset_dict['maximum_latitude'],
                        start_datetime=year_begin,
                        end_datetime=year_end,
                        output_directory=subset_dict['output_directory'],
                        output_filename=filename,
                        variables=subset_dict['variables'],
                        dry_run=False
        
    )
