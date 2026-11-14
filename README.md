# Poker Analytics Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![PyQt6](https://img.shields.io/badge/PyQt6-GUI-green.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red.svg)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Object%20Detection-orange.svg)

A desktop application for analysing poker games in real time using computer vision and machine learning.

</div>

---

## 📋 Description

**Poker Analytics Assistant** — This is an intelligent poker assistant that captures the poker table screen, recognises
cards using neural networks and calculates the mathematical odds of improving your hand in real time. The app helps you
make informed decisions whilst playing by displaying the probabilities of making various poker hands.

### Key features

- 🎯 **Real-time card detection** — detecting cards on the screen using YOLOv8
- 🧠 **Card classification** — recognition of card ranks and suits using MobileNetV3
- 📊 **Probability calculation** — mathematical analysis of the odds of improving for all poker hands
- 🖥️ **Multi-tabling** — support for tracking multiple tables simultaneously
- 🎨 **Graphical user interface** — user-friendly PyQt6 interface with visualisation of cards and statistics
- ⚡ **Optimised performance** — fast frame processing (15 FPS) with no lag

---

## 🏗️ Project architecture

```
Poker_Analytic/
├── app/                          # Core business logic
│   ├── calculating/              # Probability calculation module
│   │   ├── combinations/         # Calculators for every combination
│   │   │   ├── pair.py          # Calculating the odds for a pair
│   │   │   ├── two_pair.py      # Calculating the odds of two pairs
│   │   │   ├── set.py           # Calculating the odds of winning a set
│   │   │   ├── straight.py      # Calculating the odds of a straight
│   │   │   ├── flush.py         # Calculating the odds of a flush
│   │   │   ├── full_hause.py    # Calculating the odds of a full house
│   │   │   ├── kare.py          # Calculating the odds of a four-of-a-kind
│   │   │   ├── street_flash.py  # Calculating the odds of a straight flush
│   │   │   └── flush_royal.py   # Calculating the odds of a royal flush
│   │   ├── base_odds.py         # Base class for calculations
│   │   ├── odds_result.py       # Structure of the results
│   │   └── constants.py         # Calculation constants
│   ├── detection/               # Card detection module
│   │   ├── detect_cards.py      # YOLOv8 map detector
│   │   └── card_detect.pt       # A trained YOLO model
│   ├── classification/          # Map Classification Module
│   │   ├── class_predictor.py   # MobileNetV3 classifier
│   │   ├── best_model_crop_image.pth  # Model weights
│   │   └── label_to_card.json   # Mapping classes to cards
│   └── engine/                  # Processing engine
│       ├── cards_grouper.py     # Grouping cards by position
│       └── detection_matcher.py # Comparison of detections with classification
├── gui/                         # Graphical user interface
│   ├── main_window.py          # The main application window
│   ├── table_window.py         # A window for a single desk
│   ├── log_window.py           # Log window
│   ├── pipeline_worker.py      # Worker for background processing
│   ├── stream_desctop.py       # Screen capture stream
│   └── widgets/                # Custom widgets
│       ├── card_widget.py      # Map display widget
│       ├── odds_widget.py      # Odds display widget
│       └── info_widget.py      # Information widget
├── test/                        # Tests
├── helper_scripts/             # Support scripts (script for creating cards dataset)
├── notebooks/                   # Google Colab notebooks for model training and experimentation
│   ├─ classification/           # Classification croped images       
│   │  ├─ test_cards             # Short test data from real pocker rooms for visual test 
│   │  ├─ Cards_classification.ipynb   # Notebook for training the card classification model
│   │  └─ label_to_cards.json     # JSON mapping of labels to card classes
│   └─ detect/                    # YOLO object detection model training
│      ├─ data/                   # Dataset and configuration for YOLO training
│      │  ├─ images               # Images used for model training and validation
│      │  ├─ labels               # Bounding box annotations and class labels
│      │  ├─ data.yaml            # Dataset configuration (classes, paths, number of classes)
│      │  └─ train.txt            # List of image paths used for training
│      └─Yolo_detection           # YOLO training notebook and experiments
├── main.py                     # Entry point
└── requirements.txt            # Project dependencies
```

---

## 🛠️ Technology stack

### Machine Learning and Computer Vision

- **PyTorch** — a deep learning framework
- **YOLOv8 (Ultralytics)** — card detection in images
- **MobileNetV3** — a lightweight CNN for card classification
- **OpenCV** — image processing and pre-processing
- **NumPy** — numerical computations

### Graphical user interface

- **PyQt6** — cross-platform GUI framework
- **DXCam** — high-performance screen capture (DirectX)
- **pywin32** — working with the Windows API

### Additional tools

- **Pandas** — data structuring
- **keyboard** — keyboard event interception
- **black, flake8, isort** — code linters and formatters

---

## 🚀 Installation and commissioning

### Requirements

- Python 3.10 or later
- Windows 10/11 (for screen capture using DirectX)
- NVIDIA GPU (optional, to speed up inference)

### Installing

1. Copy repository:

```bash
git clone https://github.com/yourusername/poker-analytic.git
cd Poker_Analytic
```

2. Create a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

### Launch

```bash
python main.py
```

---

## 📖 User Guide

1. **Launch the app** — the Poker Assistant main window will open
2. **Click ‘Add Table’** — the app will prompt you to select a poker table window
3. **Hover your cursor** over the poker window and **press F8** to select it
4. **A table window will open** showing the cards and odds
5. **Play poker** — the app will automatically:
    - Recognise your cards and the community cards
    - Calculate the probabilities of improving your hand
    - Display the results in real time

### Interface

- **Cards** — displays your hand and the cards on the board
- **Odds** — a table showing the probabilities of making each hand:
    - Pair
    - Two Pair
    - Set (Three of a Kind)
    - Straight
    - Flush
    - Full House
    - Four of a Kind
    - Straight Flush
    - Royal Flush
- **Logs** — detailed information about the system’s operation

---

## 🧮 Operating algorithm

### 1. Screen capture

- Captures the selected window at 15 FPS
- Optimised via DirectX for minimal system load

### 2. Map detection (YOLOv8)

- Detects areas containing maps in the image
- Identifies bounding boxes with a confidence threshold

### 3. Card Classification (MobileNetV3)

- Extraction of card images from detected regions
- Classification of each card (52 classes: 13 ranks × 4 suits)

### 4. Grouping and Validation

- Separation of cards into ‘player’s hand’ and ‘board’ by position
- Validation of card uniqueness and the correctness of the game state

### 5. Probability calculation

- Analysis of the current situation (flop/turn)
- Counting outs (cards needed to improve the hand)
- Mathematical calculation of probabilities for each combination
- Formula: `P = 1 - ((unseen - outs) / unseen) × ((unseen - outs - 1) / (unseen - 1))`

### 6. Displaying results

- Updating the GUI with a visualisation of the cards
- Displaying an odds table with percentage probabilities

---

## 🎯 Technical solutions

### Card detection

- Use of **YOLOv8** for fast and accurate detection
- Custom trained model on a dataset of poker cards
- Confidence threshold = 0.5 to balance accuracy and completeness

### Card classification

- **MobileNetV3-Small** — a lightweight architecture for fast inference
- 52 output classes (all possible cards in the deck)
- Pre-processing: ImageNet mean/std normalisation
- Inference on the CPU at a reasonable speed

### Mathematical calculations

- Implementation of classic poker formulas
- Accounts for the number of unknown cards and cards yet to be dealt
- Separate calculators for each combination
- Inherits from the base class `BaseOddsCalculator`

### Multithreading

- Screen capture in a separate thread (`QThread`)
- Worker for processing the pipeline without blocking the GUI
- PyQt signals for safe communication between threads

---

## 📊 Examples of use

### Scenario 1: The Flop

```
Hand: A♠ K♠
Board: Q♠ J♠ 2♥

The app will display:
- Flush: 35% (9 outs)
- Straight: 32% (8 outs)
- Pair: 26% (6 outs)
- Royal Flush: 4.3% (1 out)
```

### Scenario 2: Turn

```
Hand: 7♦ 8♦
Board: 9♦ 10♦ K♠ 2♣

The app will show:
- Straight: 17.4% (4 outs on the river)
- Straight Flush: 2.2% (1 out on the river)
```

---

## 🔬 Development opportunities

- [ ] Support for various types of poker (Omaha, Stud)
- [ ] Calculation of equity against various opponent hands
- [ ] Integration with poker trackers
- [ ] Saving hand histories
- [ ] Analysis of playing patterns
- [ ] Action recommendations (fold/call/raise)
- [ ] Support for macOS and Linux
- [ ] Web version of the app

---

## 🧪 Testing

The project includes a test module in the `test/` directory. To run the tests:

```bash
pytest test/
```

---

### ⚠️ Known issue with small windows

The app may not work correctly when the poker client window is set to a small size. The main issue is a significant loss
of image quality when the cards are scaled down.

The nature of the problem:

- When the game window is small, the cards are scaled down to ~15×15 pixels
- At this resolution, it is physically impossible to extract sufficient visual information for accurate classification
- The classifier (MobileNetV3) cannot reliably distinguish a card’s rank and suit from such a low-quality image

Recommendation:
Use a medium or large poker client window, where the cards remain clear and distinguishable. The minimum recommended
card size is approximately 50×70 pixels.

Possible future solutions:

- Retraining the classifier with the addition of low-resolution augmentations
- Using a super-resolution model prior to classification
- Warning the user if the window is too small

## 📝 Coding standards

The project follows Python best practices:

- **Black** — code auto-formatting (line length: 88)
- **Flake8** — code style checking
- **isort** — sorting imports
- **Type hints** — type annotations to improve readability

Configuration in `pyproject.toml` and `.flake8`.

---

## 🤝 Contribution to the project

The project was developed to demonstrate skills in the following areas:

- Computer vision
- Machine learning
- Desktop application development
- Software architecture
- Mathematical computations

---

## 📄 Licence

This project has been created for educational purposes.

---

## 👨‍💻 Author

Developed using modern ML/CV technologies and Python.

**Contact details:**

- GitHub: [AlexeySerebryansky]
- Email: [aleksejserebranskij020@gmail.com]
- LinkedIn: [Oleksii Serebrianskyi]

---

<div align="center">

**Poker Analytics Assistant** — when mathematics meets artificial intelligence 🎰🤖

</div>
