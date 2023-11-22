class Robot:
    def __init__(self, width, height, max_v, max_a):
        self.width = width
        self.height = height
        self.max_v = max_v
        self.max_a = max_a
        self.current_motion = [0.0, 0.0, 0.0]
