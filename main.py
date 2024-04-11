import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

df = pd.read_csv("music_log.csv")


def process_table(dataframe):
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


if __name__ == "__main__":
    print(process_table(dataframe=df).isna().sum())
