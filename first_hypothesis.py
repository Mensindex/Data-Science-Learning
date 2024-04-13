import pandas as pd
from pandas import DataFrame, Series

import processing_data_frame

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)


def replace_wrong_values(
        target_column: Series, wrong_values: list[int | str], correct_value: str
):
    result = target_column.replace(to_replace=wrong_values, value=correct_value)
    return result


def get_track_list_count(df: DataFrame, day_of_the_week: str, city_name: str):
    day_df = df[df[processing_data_frame.DAY_OF_THE_WEEK] == day_of_the_week]
    day_and_city_df = day_df[day_df[processing_data_frame.CITY] == city_name]
    track_list_count = day_and_city_df[processing_data_frame.USER_ID].count()
    return track_list_count


def check_first_hypothesis():
    processed_df: DataFrame = processing_data_frame.get_processed_df()

    track_count_in_moscow_on_monday = get_track_list_count(
        df=processed_df,
        day_of_the_week="Monday",
        city_name="Moscow",
    )
    track_count_in_saint_petersburg_on_monday = get_track_list_count(
        df=processed_df,
        day_of_the_week="Monday",
        city_name="Saint-Petersburg",
    )
    track_count_in_moscow_on_wednesday = get_track_list_count(
        df=processed_df,
        day_of_the_week="Wednesday",
        city_name="Moscow",
    )
    track_count_in_saint_petersburg_on_wednesday = get_track_list_count(
        df=processed_df,
        day_of_the_week="Wednesday",
        city_name="Saint-Petersburg",
    )
    track_count_in_moscow_on_friday = get_track_list_count(
        df=processed_df,
        day_of_the_week="Friday",
        city_name="Moscow",
    )
    track_count_in_saint_petersburg_on_friday = get_track_list_count(
        df=processed_df,
        day_of_the_week="Friday",
        city_name="Saint-Petersburg",
    )
    columns = ["city", "monday", "wednesday", "friday"]
    data = [
        [
            "Saint-Petersburg",
            track_count_in_saint_petersburg_on_monday,
            track_count_in_saint_petersburg_on_wednesday,
            track_count_in_saint_petersburg_on_friday,
        ],
        [
            "Moscow",
            track_count_in_moscow_on_monday,
            track_count_in_moscow_on_wednesday,
            track_count_in_moscow_on_friday,
        ],
    ]
    result_df = pd.DataFrame(data=data, columns=columns)
    print(result_df)
