import pandas as pd
from pandas import DataFrame, Series

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)


# common const
USER_ID = "user_id"
TRACK_NAME = "track_name"
ARTIST_NAME = "artist_name"
GENRE_NAME = "genre_name"
CITY = "city_name"
LISTENING_TIME = "listening_time"
DAY_OF_THE_WEEK = "day_of_the_week"


def get_processed_df():
    processed_df = pd.read_csv("yandex_music_project.csv")

    processed_df = processed_df.rename(
        columns={
            "  userID": USER_ID,
            "Track": TRACK_NAME,
            "artist": ARTIST_NAME,
            "genre": GENRE_NAME,
            "  City  ": CITY,
            "time": LISTENING_TIME,
            "Day": DAY_OF_THE_WEEK,
        }
    )

    processed_df = processed_df.drop_duplicates().reset_index(drop=True)

    processed_df[TRACK_NAME] = processed_df[TRACK_NAME].fillna("unknown")
    processed_df[ARTIST_NAME] = processed_df[ARTIST_NAME].fillna("unknown")
    processed_df[GENRE_NAME] = processed_df[GENRE_NAME].fillna("unknown")

    processed_df[GENRE_NAME] = replace_wrong_values(
        target_column=processed_df[GENRE_NAME],
        wrong_values=["hip", "hip-hop", "hop"],
        correct_value="hiphop",
    )
    processed_df[GENRE_NAME] = replace_wrong_values(
        target_column=processed_df[GENRE_NAME],
        wrong_values=["электроника"],
        correct_value="electronic",
    )

    return processed_df


def replace_wrong_values(
    target_column: Series,
    wrong_values: list[int | str],
    correct_value: str,
):
    result = target_column.replace(to_replace=wrong_values, value=correct_value)
    return result


# Custom function to fill nan-values instead fillna() function
def fill_nan(column: Series):
    columns_to_replace = column
    for index, value in column.items():
        if pd.isnull(value):
            columns_to_replace[index] = "unknown"
    return columns_to_replace
