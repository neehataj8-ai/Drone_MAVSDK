import math

SAFE_DISTANCE = 2.0

class SafetyAnalyzer:

    def check(self, people):

        violations = []

        for i in range(len(people)):
            for j in range(i+1, len(people)):

                a = people[i]["center"]
                b = people[j]["center"]

                d = math.sqrt(
                    (a[0]-b[0])**2 +
                    (a[1]-b[1])**2
                )

                if d < 150:
                    violations.append((i, j))

        return violations