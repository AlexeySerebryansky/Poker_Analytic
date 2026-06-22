import tkinter as tk

from PIL import Image
from PIL import ImageTk

import cv2


class MainWindow:

    def __init__(self, capture, detector, collector):

        self.capture = capture
        self.detector = detector
        self.collector = collector

        self.root = tk.Tk()
        self.root.title("Poker Dataset Collector")

        self.root.geometry("1400x1080")
        self.root.minsize(1200, 700)

        self.paused = False
        self.current_frame = None
        self.display_frame = None

        self.pending_detections = []
        self.current_detection_idx = 0

        self._build_ui()
        self._bind_hotkeys()

        self.frame_generator = self.capture.stream()

        self.update_stream()

    def _build_ui(self):

        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        left_frame = tk.Frame(main_frame)
        left_frame.pack(side="left", fill="both", expand=True)

        right_frame = tk.Frame(main_frame)
        right_frame.pack(side="right", fill="y", padx=(10, 0))

        self.stream_label = tk.Label(left_frame, bg="black")

        self.stream_label.pack(fill="both", expand=True)

        self.crop_label = tk.Label(right_frame, bg="gray", relief="solid", bd=1)

        self.crop_label.pack(fill="both")

        self.progress_label = tk.Label(right_frame, text="No detections")
        self.progress_label.pack(pady=(10, 0))

        self.status_label = tk.Label(right_frame, text="Streaming")
        self.status_label.pack(pady=(10, 0))

        self.label_entry = tk.Entry(right_frame, font=("Arial", 14))
        self.label_entry.pack(fill="x", pady=(20, 0))

        self.pause_button = tk.Button(
            right_frame, text="Pause (Shift + P)", command=self.toggle_pause
        )
        self.pause_button.pack(fill="x", pady=(20, 0))

        self.detect_button = tk.Button(
            right_frame, text="Detect (Shift + D)", command=self.detect_cards
        )
        self.detect_button.pack(fill="x")

        self.save_button = tk.Button(
            right_frame, text="Save (Enter)", command=self.save_current_card
        )
        self.save_button.pack(fill="x")

        self.skip_button = tk.Button(
            right_frame, text="Skip (Shift + S)", command=self.skip_current_card
        )
        self.skip_button.pack(fill="x")

        self.quit_button = tk.Button(
            right_frame, text="Quit (Escape)", command=self.close
        )
        self.quit_button.pack(fill="x", pady=(20, 0))

        self.stats_button = tk.Button(
            right_frame, text="Statistics (F3)", command=self.show_stats
        )

        self.stats_button.pack(fill="x")

    def _bind_hotkeys(self):

        self.root.bind("<P>", lambda e: self.toggle_pause())

        self.root.bind("<D>", lambda e: self.detect_cards())

        self.root.bind("<Return>", lambda e: self.save_current_card())

        self.root.bind("<S>", lambda e: self.skip_current_card())

        self.root.bind("<Escape>", lambda e: self.close())

        self.root.bind("<F3>", lambda e: self.show_stats())

    def cv_to_tk(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        image = Image.fromarray(rgb)

        return ImageTk.PhotoImage(image)

    def update_stream(self):
        try:

            if not self.paused:

                frame = next(self.frame_generator)

                self.current_frame = frame.copy()

                if self.display_frame is None:
                    frame_to_show = frame
                else:
                    frame_to_show = self.display_frame

            else:

                if self.display_frame is not None:
                    frame_to_show = self.display_frame
                else:
                    frame_to_show = self.current_frame

            image = self.cv_to_tk(frame_to_show)

            self.stream_label.configure(image=image)

            self.stream_label.image = image

        except StopIteration:
            return

        self.root.after(30, self.update_stream)

    def toggle_pause(self):
        self.paused = not self.paused

        if not self.paused:
            self.display_frame = None

        if self.paused:

            self.status_label.config(text="Paused")
        else:
            self.status_label.config(text="Streaming")

    def detect_cards(self):
        if self.current_frame is None:
            return

        detections = self.detector.detect_cards(self.current_frame)

        self.display_frame = self.draw_detections(self.current_frame, detections)

        cv2.waitKey(1)

        detections.sort(key=lambda d: (d.y1, d.x1))

        self.pending_detections = detections
        self.current_detection_idx = 0

        self.show_current_crop()

    def draw_detections(self, frame, detections):
        draw_frame = frame.copy()

        for detection in detections:
            cv2.rectangle(
                draw_frame,
                (detection.x1, detection.y1),
                (detection.x2, detection.y2),
                (0, 255, 0),
                2,
            )
        return draw_frame

    def get_current_crop(self):
        if not self.pending_detections:
            return None

        detection = self.pending_detections[self.current_detection_idx]

        return detection.crop(self.current_frame)

    def show_current_crop(self):
        crop = self.get_current_crop()

        if crop is None:
            self.crop_label.configure(image="")

            self.progress_label.config(text="No detections")

            return

        image = self.cv_to_tk(crop)

        self.crop_label.configure(image=image)

        self.crop_label.image = image

        self.progress_label.config(
            text=(
                f"{self.current_detection_idx + 1}"
                f"/"
                f"{len(self.pending_detections)}"
            )
        )

        self.label_entry.delete(0, tk.END)

        self.label_entry.focus()

    def save_current_card(self):
        crop = self.get_current_crop()

        if crop is None:
            return

        label = self.label_entry.get().strip()

        if not label:
            return

        self.collector.save(crop=crop, label=label)

        self.next_card()

    def skip_current_card(self):
        if not self.pending_detections:
            return

        self.next_card()

    def next_card(self):
        self.current_detection_idx += 1

        if self.current_detection_idx >= len(self.pending_detections):
            self.pending_detections.clear()

            self.crop_label.configure(image="")

            self.progress_label.config(text="Done")

            return

        self.show_current_crop()

    def show_stats(self):
        stats = self.collector.get_stats()

        sorted_stats = sorted(stats.items(), key=lambda x: x[1])

        window = tk.Toplevel(self.root)

        window.title("Dataset Statistics")
        window.geometry("400x700")

        rows = []

        columns = 4

        for i in range(0, len(sorted_stats), columns):

            chunk = sorted_stats[i : i + columns]

            line = ""

            for label, count in chunk:
                line += f"{label:<3}: {count:<4}"

            rows.append(line)

        stats_text = "\n".join(rows)

        label = tk.Label(
            window, text=stats_text, justify="left", anchor="nw", font=("Consolas", 12)
        )

        label.pack(fill="both", expand=True, padx=10, pady=10)

    def close(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()
