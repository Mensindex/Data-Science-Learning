from typing import Hashable

import pandas as pd
from pandas import DataFrame
from pandas.core.groupby import DataFrameGroupBy

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

df = pd.read_csv("music_log.csv")


def process_table(dataframe: DataFrame):
    processed_df = dataframe

    # Проверяем количество строк и столбцов таблицы
    # print(processed_df.shape)

    # Проверяем первые элементы таблицы
    # print(processed_df.head(15))

    # Проверяем имена колонок
    # print(processed_df.columns)
    # Переименовываем колонки в единый стиль
    processed_df = processed_df.rename(
        columns={
            "  user_id": "user_id",
            "total play": "total_play_seconds",
            "Artist": "artist_name",
            "genre": "genre_name",
            "track": "track_name",
        }
    )

    # Проверяем таблицу на дубликаты
    # print(processed_df.duplicated().sum())
    # Очищаем таблицу от дубликатов без сохранения колонки старых индексов
    processed_df = processed_df.drop_duplicates().reset_index(drop=True)

    # Проверяем таблицу на пустые значения
    # print(processed_df.isna().sum())
    # Заполняем пустые значения колонки total_play нулями
    processed_df["total_play_seconds"] = processed_df["total_play_seconds"].fillna(0)
    # Заменяем пустые значения в track_name и artist_name на unknown
    processed_df["track_name"] = processed_df["track_name"].fillna("unknown")
    processed_df["artist_name"] = processed_df["artist_name"].fillna("unknown")
    # Удаляем все строки, где в колонке genre_name содержатся пустые значения
    processed_df = processed_df.dropna(subset=["genre_name"])

    # Проверяем на уникальность значения в колонке genre_name
    # print(processed_df["genre_name"].unique())
    # Заменяем похожие значения на аналогичные, соответствующие остальному стилю
    processed_df["genre_name"] = processed_df["genre_name"].replace(
        "электроника", "electronic"
    )
    # Убеждаемся, что значений "электроника" не осталось
    # print(processed_df[processed_df["genre_name"] == "электроника"]["genre_name"].count())
    return processed_df


def get_group_by_genre(processed_df: DataFrame):
    # Очищаем от значений, где пользователь скипнул трек
    df_drop_null = processed_df[processed_df["total_play_seconds"] != 0]
    # Группируем таблицу по пользователям и выбираем колонку genre_name как показатель для сравнения
    genre_grouping = df_drop_null.groupby(by="user_id")["genre_name"]
    return genre_grouping


def find_more_fifty_songs_listener(group_by_genre: DataFrameGroupBy):
    for col in group_by_genre:
        if len(col[1]) > 50:
            user = col[0]
            return user


def find_meloman_id(processed_df: DataFrame):
    genre_grouping = get_group_by_genre(processed_df=processed_df)
    meloman_id = find_more_fifty_songs_listener(group_by_genre=genre_grouping)
    return meloman_id


def get_meloman_tracks_without_null(processed_df: DataFrame, meloman_id: Hashable):
    meloman_tracks_df = processed_df[processed_df["user_id"] == meloman_id]
    meloman_tracks_without_null = meloman_tracks_df[
        meloman_tracks_df["total_play_seconds"] > 0
    ]
    return meloman_tracks_without_null


def get_sum_meloman_tracks(meloman_tracks_df: DataFrame):
    sum_meloman_tracks = meloman_tracks_df.groupby(by="genre_name")["total_play_seconds"].sum()
    return sum_meloman_tracks


def get_count_meloman_tracks(meloman_tracks_df: DataFrame):
    count_meloman_tracks = meloman_tracks_df.groupby(by="genre_name")["genre_name"].count()
    return count_meloman_tracks


def get_sorted_sum_meloman_tracks(sum_meloman_tracks_df: DataFrame):
    sorted_sum_meloman_tracks = sum_meloman_tracks_df.sort_values(ascending=False)
    return sorted_sum_meloman_tracks


def get_sorted_count_meloman_tracks(count_meloman_tracks_df: DataFrame):
    sorted_count_meloman_tracks = count_meloman_tracks_df.sort_values(ascending=False)
    return sorted_count_meloman_tracks


if __name__ == "__main__":
    processed_table = process_table(dataframe=df)
    meloman_id = find_meloman_id(processed_df=processed_table)
    meloman_tracks = get_meloman_tracks_without_null(
        processed_df=processed_table, meloman_id=meloman_id
    )
    sum_meloman_tracks = get_sum_meloman_tracks(meloman_tracks_df=meloman_tracks)
    count_meloman_tracks = get_count_meloman_tracks(meloman_tracks_df=meloman_tracks)
    sorted_sum_meloman_tracks = get_sorted_sum_meloman_tracks(sum_meloman_tracks_df=sum_meloman_tracks)
    sorted_count_meloman_tracks = get_sorted_count_meloman_tracks(
        count_meloman_tracks_df=count_meloman_tracks
    )
    print(sorted_sum_meloman_tracks)
