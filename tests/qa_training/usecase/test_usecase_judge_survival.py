import os

from qa_training.utils.boundary.usecase.if_usecase_judge_survival import (
    IF_UsecaseJudgeSurvival,
)


def test_judge_survival(fixture_judge_survival: IF_UsecaseJudgeSurvival):
    usecase_judge_survival = fixture_judge_survival

    usecase_judge_survival.judge_survival()

    assert os.path.exists("tests/output/df_results.csv")
