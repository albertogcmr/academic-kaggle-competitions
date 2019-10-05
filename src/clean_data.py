import pandas as pd

def clean_data(data_frame):

    # Cylinders
    print('Cleaning cylinders...')
    # Electric cars will have null values, will set those to zero.
    # Change nulls to other
    data_frame['cylinders'] = data_frame['cylinders'].str.replace(' cylinders', '')

    null_cylinders = data_frame[data_frame['cylinders'].isnull()]
    for index, car in null_cylinders.iterrows():
        if car['fuel'] == 'electric':
            data_frame.at[index,'cylinders'] = 0
        else:
            data_frame.at[index,'cylinders'] = 'other'
    # Check mean and median of cylinders
    # Change to numeric
    not_null_cylinders = data_frame[data_frame['cylinders'] != 'other']['cylinders']
    not_null_cylinders = not_null_cylinders.apply(int)
    mean = not_null_cylinders.mean()
    median = not_null_cylinders.median()
    # Change 'other' for median
    data_frame['cylinders'][data_frame['cylinders']=='other'] = median
    data_frame['cylinders'] = data_frame['cylinders'].astype('int64')
    
    # Condition
    print('Cleaning condition...')
    # Will change to numeric and convert nulls to central number
    data_frame['condition'][data_frame['condition'].isnull()] = 'unknown'
    condition = {'unknown':0,'fair':0,'good':1,'excellent':2,'like new':2,'new':2,'salvage':-1}
    data_frame['condition']=data_frame['condition'].apply(lambda x: condition.get(x,0))
    
    # Odometer
    print('Cleaning odometer...')
    # Will check mean and median by year
    # First, clean year.
    # Replace unknown and wrong years by average
    valid_year = data_frame['year'][((data_frame['year']>=1900) | (~data_frame['year'].isnull()))]
    year_avg = valid_year.mean()
    year_median = valid_year.median()
    year_mode = valid_year.mode()
    data_frame['year'][((data_frame['year']<1900) | (data_frame['year'].isnull()))] = year_avg
    # Replace Null odometer by mean of decade or absolute mean
    data_frame['decade'] = data_frame['year']//10
    null_odometer = data_frame[data_frame['odometer'].isnull()]
    odometer_by_decade_mean = data_frame[['decade','odometer']].groupby(by='decade').mean()
    odometer_by_decade_median = data_frame[['decade','odometer']].groupby(by='decade').median()
    odometer_mean = data_frame['odometer'].mean()
    for index, car in null_odometer.iterrows():
        data_frame.at[index,'odometer'] = odometer_by_decade_mean.get(car['decade'],odometer_mean)
    
    # Drive
    print('Cleaning drive...')
    # Replace unknown with fwd, as it is the most comon drive
    data_frame['drive'][data_frame['drive'].isnull()]='fwd'
    
    # Size
    print('Cleaning size...')
    # Replace unknown with most common by cylinders
    null_size = data_frame[data_frame['size'].isnull()]
    size_by_cylinder = data_frame[['size','cylinders']].groupby(by='cylinders').agg(lambda x:x.value_counts().index[0])
    size_by_cylinder = {cyl:size for cyl,size in zip(size_by_cylinder.index,size_by_cylinder['size'])}
    for index, car in null_size.iterrows():
        data_frame.at[index,'size'] = size_by_cylinder.get(car['cylinders'],'other')

    # Manufacturer
    print('Cleaning manufacturer...')
    # Fix multiple values
    manufacturer = {'chevy':'chevrolet','chev':'chevrolet','vw':'volkswagen','mercedes':'mercedes-benz','mercedesbenz':'mercedes-benz','infinity':'infiniti','harley':'harley-davidson','alfa':'alfa-romeo','aston':'aston-martin','landrover':'land rover','rover':'land rover'}
    wrong_manufacturers = data_frame[data_frame['manufacturer'].isin(manufacturer.keys())]
    for index, car in wrong_manufacturers.iterrows():
        data_frame.at[index,'manufacturer'] = manufacturer.get(car['manufacturer'],'unknown')
    # Replace null with unknown
    data_frame['manufacturer'][data_frame['manufacturer'].isnull()] = 'unknown'
        
    # Fuel
    print('Cleaning fuel...')
    # Replace Null with 'other'
    data_frame['fuel'][data_frame['fuel'].isnull()]='other'

    # Transmission
    print('Cleaning transmission...')
    data_frame['transmission'][data_frame['transmission'].isnull()]='other'

    # Title Status
    print('Cleaning title status...')
    data_frame['title_status'][data_frame['title_status'].isnull()]='clean'

    # Return cleaned data_frame
    print('Data cleaning complete!')
    return data_frame

def prepare_data(data_frame):
    # Select only relevant columns
    data_frame = data_frame[['year','manufacturer','condition','cylinders','fuel','odometer','title_status','transmission','drive','size']]
    # Getting dummies for categorical columns
    data_frame = pd.get_dummies(data_frame,drop_first=True)
    # Get X and y
    X = data_frame
    return X