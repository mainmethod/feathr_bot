import mock
from feathr_bot.services.analyze_service import AnalyzeService


@mock.patch("feathr_bot.services.analyze_service.OpenAIService.analyze")
def test_analyze(mock_analyze, analyze_response):
    prompt = "This is a super postive email"
    expected_result = "Positive"
    mock_analyze.return_value = analyze_response

    result = AnalyzeService(prompt=prompt).analyze()

    assert expected_result == result
    mock_analyze.assert_called_once_with(
        f"Classify the sentiment in this email:\n\n{prompt}"
    )
