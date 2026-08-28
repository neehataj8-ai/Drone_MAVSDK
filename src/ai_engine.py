class AIEngine:

    def decide(self, people):

        if len(people) == 0:
            return "NO_PERSON"

        if len(people) == 1:
            return "TRACK"

        return "MULTIPLE_TARGETS"