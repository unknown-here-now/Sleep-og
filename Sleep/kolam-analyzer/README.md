# Kolam Analyzer

## Overview
The Kolam Analyzer is a Python project designed to analyze images of Kolam designs, detect various shapes such as hexagons, petals, diamonds, and dots, and recreate the design using the Turtle graphics module. This project utilizes image processing libraries like OpenCV and Pillow for effective shape detection.

## Project Structure
```
kolam-analyzer
├── src
│   ├── main.py
│   ├── image_processing.py
│   ├── shape_detection.py
│   ├── kolam_turtle.py
│   └── utils.py
├── requirements.txt
├── README.md
└── examples
    └── sample_kolam.jpg
```

## Requirements
To run this project, you need to install the following Python libraries:
- OpenCV
- Pillow
- turtle (included in standard Python library)

You can install the required libraries using pip. Create a virtual environment and run:
```
pip install -r requirements.txt
```

## Setup Instructions
1. **Clone the Repository**: 
   Clone this repository to your local machine using:
   ```
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**:
   ```
   cd kolam-analyzer
   ```

3. **Install Dependencies**:
   Make sure you have Python installed. Then, install the required libraries:
   ```
   pip install -r requirements.txt
   ```

4. **Prepare Your Image**:
   Place your Kolam design image in the `examples` directory. You can use the provided `sample_kolam.jpg` for testing.

## Running the Program
To run the Kolam Analyzer, execute the following command:
```
python src/main.py examples/sample_kolam.jpg
```
Replace `examples/sample_kolam.jpg` with the path to your own image if desired.

## How It Works
1. **Image Loading**: The program loads the specified image using functions from `image_processing.py`.
2. **Preprocessing**: The image is converted to grayscale and edge detection is applied to highlight shapes.
3. **Shape Detection**: The processed image is analyzed to detect shapes using functions from `shape_detection.py`.
4. **Drawing with Turtle**: Detected shapes are drawn using the Turtle graphics module, with configurations set in `kolam_turtle.py`.

## Example
You can find a sample Kolam design in the `examples` folder. Run the program with this image to see how it detects and recreates the design.

## Contributing
Feel free to contribute to this project by submitting issues or pull requests. Your feedback and contributions are welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for more details.