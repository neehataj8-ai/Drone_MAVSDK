class Predictor:

    def predict(self,history):

        if len(history)<2:
            return history[-1]

        x1,y1 = history[-2]
        x2,y2 = history[-1]

        dx = x2-x1
        dy = y2-y1

        return (
            x2+dx,
            y2+dy
        )