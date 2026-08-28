from ultralytics.trackers.byte_tracker import BYTETracker

class Tracker:

    def __init__(self):

        self.tracker = BYTETracker()

    def update(self, results):

        tracks = self.tracker.update(results)

        return tracks