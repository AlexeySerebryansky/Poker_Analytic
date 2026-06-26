class TableStreamer:

    def __init__(self, screen_stream, table_window):
        self.screen_stream = screen_stream
        self.table_window = table_window

    @property
    def frame_number(self):
        return self.screen_stream.frame_number

    @property
    def latest_frame(self):

        frame = self.screen_stream.latest_frame

        if frame is None:
            return None

        x1, y1, x2, y2 = self.table_window.region

        return frame[y1:y2, x1:x2]

