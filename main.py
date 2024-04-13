import pandas as pd

import first_hypothesis
import second_hypothesis
import third_hypothesis

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

if __name__ == "__main__":
    print()
    print()
    print("-----------------------------------First hypothesis-----------------------------------")
    print()
    first_hypothesis.check_first_hypothesis()
    print()
    print()
    print("-----------------------------------Second hypothesis-----------------------------------")
    print()
    second_hypothesis.check_second_hypothesis()
    print()
    print()
    print("-----------------------------------Third hypothesis-----------------------------------")
    print()
    third_hypothesis.check_third_hypothesis()
