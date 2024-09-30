from collections import Counter
import emoji
import time
import logging
from memory_profiler import memory_usage
from typing import List, Tuple

class TweetAnalytics:
    def __init__(self, data):
        self.data = data

    def q1_top_dates(self, top_n: int = 10) -> List[Tuple]:
        """Get the 10 dates with the most tweets and the user with the most tweets on each date."""
        start_time = time.time()
        top_dates = self.data.groupby('date').size().nlargest(top_n).index
        result = []
        for date in top_dates:
            user = self.data[self.data['date'] == date].groupby('user').size().idxmax()
            result.append((date, user))
        logging.info(f"Execution time for q1: {time.time() - start_time} seconds")
        return result

    def q2_top_emojis(self, top_n: int = 10) -> List[Tuple[str, int]]:
        """Get the 10 most used emojis."""
        def extract_emojis(text):
            return [char for char in text if char in emoji.UNICODE_EMOJI['en']]

        start_time = time.time()
        self.data['emojis'] = self.data['text'].apply(extract_emojis)
        all_emojis = [emoji for sublist in self.data['emojis'] for emoji in sublist]
        top_emojis = Counter(all_emojis).most_common(top_n)
        logging.info(f"Execution time for q2: {time.time() - start_time} seconds")
        return top_emojis

    def q3_top_mentions(self, top_n: int = 10) -> List[Tuple[str, int]]:
        """Get the 10 most mentioned users."""
        def extract_mentions(text):
            return [word for word in text.split() if word.startswith('@')]

        start_time = time.time()
        self.data['mentions'] = self.data['text'].apply(extract_mentions)
        all_mentions = [mention for sublist in self.data['mentions'] for mention in sublist]
        top_mentions = Counter(all_mentions).most_common(top_n)
        logging.info(f"Execution time for q3: {time.time() - start_time} seconds")
        return top_mentions

    def measure_memory(self, function, *args):
        """Measure memory used by a function."""
        memory_used = memory_usage((function, args), max_iterations=1)
        logging.info(f"Memory used: {memory_used} MiB")
        return memory_used
