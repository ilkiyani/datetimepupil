import pathlib
import json

import numpy as np
import pandas as pd

pd.options.display.float_format = '{:}'.format

DATAFRAME_HEAD_COUNT = 3
rec_dir = pathlib.Path.cwd().joinpath("recordings").joinpath("2022_11_07").joinpath("001").absolute()
assert rec_dir.is_dir(), "Please download the sample recording into 'recordings' directory."
rec_dir
export_dir = rec_dir.joinpath("exports").joinpath("002")
assert export_dir.is_dir(), "Please create at least one export."
export_dir
with rec_dir.joinpath("info.player.json").open() as file:
    meta_info = json.load(file)

meta_info
start_timestamp_unix = meta_info["start_time_system_s"]
start_timestamp_pupil = meta_info["start_time_synced_s"]
start_timestamp_diff = start_timestamp_unix - start_timestamp_pupil
pupil_positions_df = pd.read_csv(export_dir.joinpath("pupil_positions.csv"))
pupil_positions_df.head(DATAFRAME_HEAD_COUNT)
pupil_positions_df["pupil_timestamp_unix"] = pupil_positions_df["pupil_timestamp"] + start_timestamp_diff
pupil_positions_df.head(DATAFRAME_HEAD_COUNT)
pupil_positions_df["pupil_timestamp_datetime"] = pd.to_datetime(pupil_positions_df["pupil_timestamp_unix"], unit="s")
pupil_positions_df.head(DATAFRAME_HEAD_COUNT)
pupil_positions_df.to_csv(export_dir.joinpath("pupil_positions_unix_datetime.csv"))
gaze_positions_df = pd.read_csv(export_dir.joinpath("gaze_positions.csv"))
gaze_positions_df["gaze_timestamp_unix"] = gaze_positions_df["gaze_timestamp"] + start_timestamp_diff
gaze_positions_df["gaze_timestamp_datetime"] = pd.to_datetime(gaze_positions_df["gaze_timestamp_unix"], unit="s")
gaze_positions_df.to_csv(export_dir.joinpath("gaze_positions_unix_datetime.csv"))
gaze_positions_df.head(DATAFRAME_HEAD_COUNT)
