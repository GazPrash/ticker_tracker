# for command line interfaces
from tickers import Ticker


def main():

    tic:str = input('Enter a valid ticker')
    tic_primary = Ticker(tic)
    if (tic_primary.find_dataframe()).empty:
        raise Exception('We don not have any information regarding the requested ticker/stock')


    mode:str = input('Would you like to analyze the latest results? (Y/n')
    if mode.lower() == 'y':
        t_range:str = '1d'
        interval:str = '30m'

    else:
        t_range:str = input('Select & Enter a valid timeframe (1d/5d/1mo/3mo/1y/max)')
        interval:str = input('Select & Enter a valid time interval (5m/15m/30m/90m/1h/1d)')

    print("""
        1. Download CSV
        2. Analyze Data
        3. Compare with...  
    """)

    task:int = int(input('Please choose an option from above (Enter the index number of your choice')) 

    if task == 1:
        df = tic_primary.find_dataframe()
        df.to_csv(f'Downloads/{tic} Stocks/')

    elif task == 2:
        print("""
            1. Line Plot
            2. Bar Plot
            3. Linear Regression Plot
            4. Violin Plot
            5. Violin Plot (w/ Swarm)
            6. Box Plot
            7. Empirical Cumulative Desnity Frequency Plot
        
        """)
        anls_mode:int = int(input('Please choose an option from above (Enter the index number of your choice'))

        if anls_mode == 1:
            plot_style = 'plot'
        elif anls_mode == 2:
            plot_style = 'bar'
        elif anls_mode == 3:
            plot_style = 'reg'
        elif anls_mode == 4:
            plot_style = 'vio'
        elif anls_mode == 5:
            plot_style = 'vios'
        elif anls_mode == 6:
            plot_style = 'box'
        elif anls_mode == 7:
            plot_style = 'ecdf'

        plot_img = tic_primary.plot_analysis(kind = plot_style)
        plot_img.save(f'Downloads/{tic} Analysis')
    
    elif task == 3:
        tic2:str = input('Enter an another valid ticker')
        tic_sec = Ticker(tic2)
        if (tic_sec.find_dataframe()).empty:
            raise Exception('We don not have any information regarding the requested ticker/stock')

        ...
        


    


    



if __name__ == "__main__":
    main()

