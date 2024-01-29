import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'] )

# Clean data
df = df[ ( df['value'] > df['value'].quantile(0.025) ) 
 & ( df['value'] < df['value'].quantile(0.975) )]


def draw_line_plot():
    plt.clf()
    # Draw line plot
    ax = sns.lineplot( data=df, x='date', y='value' )
    ax.set_title( 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019' )
    ax.set_xlabel( 'Date' )
    ax.set_ylabel( 'Page Views' )


    fig = ax.figure
    fig.set_facecolor( 'white' )
    fig.set_size_inches( (20,5) )

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    sns.reset_defaults()
    plt.clf()
    
    FONTSIZE = 23

    # Copy and modify data for monthly bar plot
  
    Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # df_bar should be the average page views per month
    # df_bar = pd.DataFrame( df.groupby( pd.PeriodIndex( df['date'], freq='M' ) )['value'].mean() )
    df_bar = df.groupby( pd.PeriodIndex( df['date'], freq='M' ) ).aggregate( 'mean' )
    # Draw bar plot
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.to_timestamp().month_name()
    
    ax = sns.barplot( data = df_bar,
                      hue='month',
                      y='value',
                      x='year',
                      palette=sns.color_palette(n_colors=12),
                      hue_order=Months,
                      width=.5)
    
    ax.set_xlabel('Years', fontsize=FONTSIZE)
    ax.set_ylabel('Average Page Views', fontsize = FONTSIZE)
    ax.set_xticklabels( ax.get_xticklabels(), rotation=90, fontsize=FONTSIZE )
    ax.set_yticklabels( ax.get_yticklabels() , fontsize=FONTSIZE )
    ax.legend( title='Months', title_fontsize = FONTSIZE, fontsize = FONTSIZE )
    
    

    fig = ax.figure
    fig.set_facecolor( "white" )
    fig.set_size_inches([17,15])
    
    # print( len([rect for rect in ax.get_children() if isinstance(rect, mpl.patches.Rectangle)]) )
    # print(df_bar)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig
  
def draw_box_plot():
    plt.clf()
  
    Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
  
    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots( 1, 2, figsize=( 30, 10 ) )
    sns.boxplot( ax = axes[0], data=df_box,
                x = 'year',
                y = 'value',
                hue = 'year',
                legend = '',
                palette = sns.color_palette( n_colors=4 )
                ).set_xlabel( 'Year' )
  
    axes[0].set_ylabel( 'Page Views' )
    axes[0].set_title('Year-wise Box Plot (Trend)')
  
    sns.boxplot(ax = axes[1],
                data = df_box,
                order = Months,
                hue_order=Months,
                x = 'month',
                y = 'value',
                hue = 'month',
                # order =  Months,
                ).set_xlabel( 'Month' )
  
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_ylabel( 'Page Views' )
  
  
    # print(df_box)
  
  
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig