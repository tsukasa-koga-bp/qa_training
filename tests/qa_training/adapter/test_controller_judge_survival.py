import os

from qa_training.adapter.controller_judge_survival import ControllerJudgeSurvival


def test_run(fixture_judge_survival: ControllerJudgeSurvival):
    controller_judge_survival = fixture_judge_survival
    controller_judge_survival.run()

    assert os.path.exists("tests/output/df_results.csv")
