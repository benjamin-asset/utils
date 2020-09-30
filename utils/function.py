from enum import Enum
import pandas as pd
from pandas import Series, DataFrame


class Method(Enum):
    average = 1
    min = 2
    max = 3
    first = 4
    dense = 5


class Function:

    @staticmethod
    def get_max(value: Series, day: int) -> Series:
        max_value = value.rolling(window=day, min_periods=day).apply(
            lambda x: Series(x).max())
        return Series(max_value)

    @staticmethod
    def get_min(value: Series, day: int) -> Series:
        min_value = value.rolling(window=day, min_periods=day).apply(
            lambda x: Series(x).min())
        return Series(min_value)

    @staticmethod
    def get_median(value: Series, day: int) -> Series:
        median = value.rolling(window=day, min_periods=day).apply(
            lambda x: Series(x).median())
        return median

    @staticmethod
    def get_argmax(value: Series, day: int) -> Series:
        argmax = value.rolling(window=day, min_periods=day).apply(
            lambda x: Series(x).argmax())
        return Series(argmax)

    @staticmethod
    def get_argmin(value: Series, day: int) -> Series:
        argmin = value.rolling(window=day, min_periods=day).apply(
            lambda x: Series(x).argmin())
        return Series(argmin)

    @staticmethod
    def get_quantile(value: Series, day: int, q: float) -> Series:
        quantile = value.rolling(window=day, min_periods=day).apply(
            lambda x: Series(x).quantile(q=q))
        return quantile

    @staticmethod
    def get_pct_change(value: Series, day: int) -> Series:
        pct_change = value.pct_change(periods=day)
        return pct_change

    @staticmethod
    def get_ts_rank(value: Series, day: int, method: Method = Method.average) -> Series:
        """
            method{‘average’, ‘min’, ‘max’, ‘first’, ‘dense’}, default ‘average’
            How to rank the group of records that have the same value (i.e. ties):
                average: average rank of the group
                min: lowest rank in the group
                max: highest rank in the group
                first: ranks assigned in order they appear in the array
                dense: like ‘min’, but rank always increases by 1 between groups.
        """
        ts_rank = value.rolling(window=day, min_periods=day).apply(
            lambda x: Series(x).rank(pct=True, method=method.name).iloc[-1])
        return ts_rank

    @staticmethod
    def get_ts_zscore(value: Series, day: int) -> Series:
        """
            using ddof = 0 or ddof = 1?
        """
        ts_zscore = value.rolling(window=day, min_periods=day).apply(
            lambda x: (Series(x).iloc[-1] - Series(x).mean()) / Series(x).std(ddof=1))
        return ts_zscore

    @staticmethod
    def get_ts_skew(value: Series, day: int) -> Series:
        ts_skew = value.rolling(window=day, min_periods=day).apply(
            lambda x: Series(x).skew())
        return ts_skew

    @staticmethod
    def get_ts_kurtosis(value: Series, day: int) -> Series:
        ts_kurtosis = value.rolling(window=day, min_periods=day).apply(
            lambda x: Series(x).kurtosis())
        return ts_kurtosis

    @staticmethod
    def get_ts_regression(value: Series, day: int) -> Series:
        pass

    @staticmethod
    def get_correlation():
        pass

    @staticmethod
    def truncate(value: Series, turning_value: int) -> Series:
        return value.where(value > turning_value)

    @staticmethod
    def backfill(value: Series, change_value: int or float) -> Series:
        return value.fillna(change_value)

    @staticmethod
    def ts_backfill(value: Series) -> Series:
        ts_backfill = value.fillna(method='ffill')
        return ts_backfill