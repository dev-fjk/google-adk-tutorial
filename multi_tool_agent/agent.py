import datetime
from zoneinfo import ZoneInfo

from google.adk.agents import Agent


def get_weather(city: str) -> dict:
    """指定された都市の現在の天気予報を取得します。
    Args:
        city (str): 天気予報を取得したい都市名。
    Returns:
        dict: 成功時は status と report、失敗時はエラーメッセージを含む。
    """
    if city.lower() == "ニューヨーク":
        return {
            "status": "success",
            "report": (
                "ニューヨークの天気は晴れで、気温は摂氏25度（華氏77度）です。"
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"都市 '{city}' の天気情報は利用できません。",
        }


def get_current_time(city: str) -> dict:
    """指定された都市の現在時刻を返します。
    Args:
        city (str): 時刻を取得したい都市名。
    Returns:
        dict: 成功時は status と report、失敗時はエラーメッセージを含む。
    """

    if city.lower() == "ニューヨーク":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"申し訳ありません。{city} のタイムゾーン情報は持っていません。"
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'{city} の現在時刻は {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")} です。'
    )
    return {"status": "success", "report": report}


root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.5-flash-lite",
    description=(
        "都市の時刻と天気に関する質問に答えるエージェント。"
    ),
    instruction=(
        "あなたは親切なエージェントであり、ユーザーの都市の時刻と天気に関する質問に答えます。"
    ),
    tools=[get_weather, get_current_time],
)
