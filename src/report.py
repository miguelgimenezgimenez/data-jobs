import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
df = pd.read_csv('./input/world_data.csv')


def save_city_plots(city):
        city_data = df[df['city'] == city]

        country = city_data['country'].iloc[0]
        country_data = df[df['country'] == country]

        grouped_by_city = country_data.groupby(["city"]).size().reset_index(
        name='count').sort_values(by='count', ascending=False)
        grouped_by_tags = city_data.groupby(['tags']).size().reset_index(
        name='count').sort_values(by='count', ascending=False)
        world_wide_tags = df.groupby(['tags']).size().reset_index(
         name='count').sort_values(by='count', ascending=False)

        fig, axs = plt.subplots(3, 1, figsize=(20, 3*20))
        plot_data = [
           {
                "labels": world_wide_tags['tags'],
                "sizes": world_wide_tags['count'],
                "title": "Worldwide Jobs"
            },
           {
                "labels": grouped_by_city['city'],
                "sizes": grouped_by_city['count'],
                "title": f"Jobs Per city in {country}"
            },
           {
                "labels": grouped_by_tags['tags'],
                "sizes": grouped_by_tags['count'],
                "title":f"Job listings in {city}"
            },

           ]

        for i, ax in enumerate(axs):

            current = plot_data[i]
            labels = current['labels'][:10].append(pd.Series('other'))
            main_counts = current['sizes'][:10]
            other_counts = current['sizes'][10:].count()
            sizes = main_counts.append(pd.Series(other_counts))
            ax.pie(sizes, labels=labels, startangle=45)
            ax.set_title(current['title'])
        fig.savefig(f'./output/{city}')
