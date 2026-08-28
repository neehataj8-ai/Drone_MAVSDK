class TargetSelector:

    def select(self, tracks):

        if len(tracks) == 0:
            return None

        target = max(
            tracks,
            key=lambda t: t.tlwh[2] * t.tlwh[3]
        )

        return target