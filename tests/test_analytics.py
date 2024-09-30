import pytest
import pandas as pd
from analytics import TweetAnalytics

@pytest.fixture
def test_data():
    """Create a test DataFrame with simulated data."""
    data = {
        'date': ['2024-09-01', '2024-09-01', '2024-09-02', '2024-09-02', '2024-09-02'],
        'user': ['user1', 'user2', 'user1', 'user3', 'user3'],
        'text': ['Hello ✈️', 'Goodbye ❤️', '@user1 ✈️', '😊', '@user1 and @user2'],
    }
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date']).dt.date  # Normalize dates
    return df

def test_q1_top_dates(test_data):
    analytics = TweetAnalytics(test_data)
    result = analytics.q1_top_dates(top_n=2)
    expected = [(pd.to_datetime('2024-09-02').date(), 'user3'), (pd.to_datetime('2024-09-01').date(), 'user1')]
    assert result == expected

def test_q2_top_emojis(test_data):
    analytics = TweetAnalytics(test_data)
    result = analytics.q2_top_emojis(top_n=2)
    expected = [('✈️', 2), ('❤️', 1)]
    assert result == expected

def test_q3_top_mentions(test_data):
    analytics = TweetAnalytics(test_data)
    result = analytics.q3_top_mentions(top_n=2)
    expected = [('@user1', 2), ('@user2', 1)]
    assert result == expected
