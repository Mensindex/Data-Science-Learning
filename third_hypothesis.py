import pandas as pd

import processing_data_frame
import second_hypothesis

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

moscow_general = second_hypothesis.moscow_general
spb_general = second_hypothesis.spb_general


def get_moscow_genres():
    moscow_genres = moscow_general.groupby(by=processing_data_frame.GENRE_NAME)[
        processing_data_frame.GENRE_NAME].count()
    return moscow_genres.sort_values(ascending=False)


def get_spb_genres():
    spb_genres = spb_general.groupby(by=processing_data_frame.GENRE_NAME)[processing_data_frame.GENRE_NAME].count()
    return spb_genres.sort_values(ascending=False)


def check_third_hypothesis():
    print(get_moscow_genres().head(10))
    print()
    print(get_spb_genres().head(10))
