import pandas as pd
from pandas import DataFrame

import processing_data_frame

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

df = processing_data_frame.get_processed_df()
moscow_general = df[df[processing_data_frame.CITY] == "Moscow"]
spb_general = df[df[processing_data_frame.CITY] == "Saint-Petersburg"]


def get_top_genre_weekday(
    dataframe: DataFrame,
    day_of_the_week: str,
    start_time_mark: str,
    end_time_mark: str,
):
    genre_df = dataframe[
        dataframe[processing_data_frame.DAY_OF_THE_WEEK] == day_of_the_week
    ]
    genre_df = genre_df[
        genre_df[processing_data_frame.LISTENING_TIME] > start_time_mark
    ]
    genre_df = genre_df[genre_df[processing_data_frame.LISTENING_TIME] < end_time_mark]

    genre_df_count = genre_df.groupby(by=processing_data_frame.GENRE_NAME)[
        processing_data_frame.TRACK_NAME
    ].count()

    genre_df_sorted = genre_df_count.sort_values(ascending=False)
    return genre_df_sorted


def check_second_hypothesis():
    print(
        get_top_genre_weekday(
            dataframe=moscow_general,
            day_of_the_week="Monday",
            start_time_mark="07:00",
            end_time_mark="11:00",
        ).head(10)
    )
    print()
    print(
        get_top_genre_weekday(
            dataframe=spb_general,
            day_of_the_week="Monday",
            start_time_mark="07:00",
            end_time_mark="11:00",
        ).head(10)
    )
    print("-------------------------------")
    print(
        get_top_genre_weekday(
            dataframe=moscow_general,
            day_of_the_week="Friday",
            start_time_mark="17:00",
            end_time_mark="23:00",
        ).head(10)
    )
    print()
    print(
        get_top_genre_weekday(
            dataframe=spb_general,
            day_of_the_week="Friday",
            start_time_mark="17:00",
            end_time_mark="23:00",
        ).head(10)
    )
