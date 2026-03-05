# Shoe Sizer

Python-based tool for shoe size estimation, using an interactive web interface built with Gradio.

## Description

Shoe Sizer allows users to easily get shoe size recommendations. The project uses Gradio for the frontend, facilitating interaction with the processing logic in Python.

## Installation

The project uses Python 3.12.

1. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```

2. Install dependencies (if necessary):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the application:

```bash
python app.py
# Note: Replace 'app.py' with the name of your main script if different.
```

## Architecture

### Data Flow
This diagram shows how data moves from the user to the final size prediction.

```mermaid
flowchart LR
    U[User] -->|Image or measurements| G[Gradio interface]
    G -->|Processing| M[Model logic]
    M -->|Computation| P[Size prediction]
    P -->|Result| G
```

### Pipeline Architecture
Pipeline observed in the `experiments` notebooks to estimate size from an image.

```mermaid
flowchart TD
    I[Foot image with coin]
    D[YOLO detection for coin and foot]
    P[Center reference points]
    G[SAM guided segmentation]
    B[Bounding boxes from masks]
    F[Features width height coin_width coin_height foot_width]
    C[Calibration with coin diameter 25.5 mm]
    M[XGBoost regression model]
    O[Predicted size_cm]
    E[EU size conversion]

    I --> D --> P --> G --> B --> F --> C --> M --> O --> E
```

## Authors


| Avatar | Name | Role | Links |
|---|---|---|---|
| <img src="https://media.licdn.com/dms/image/v2/D5603AQGMRNUDZ2oHSg/profile-displayphoto-shrink_800_800/B56ZW2EgVTGUAc-/0/1742516389753?e=1774483200&v=beta&t=U9HLdPOT8cOJBQEQ2Big1HAsY60Hssy7o8zPxfG5g74" width="60" alt="Diana" style="border-radius: 50%;" /> | Diana Sánchez | Full Stack & Data Scientist |[LinkedIn](https://www.linkedin.com/in/diana-sanchez-ordonez/) |
| <img src="https://media.licdn.com/dms/image/v2/D4E35AQFJQQe7U6XKpg/profile-framedphoto-shrink_800_800/B4EZwRcEroIIAg-/0/1769819098121?e=1773352800&v=beta&t=IxfavChM1l4rAK2yX-YdJkKjagciJlvJxWvupQYMeZ8" width="60" alt="Robert" style="border-radius: 50%;" /> | Robert J. Buleje| DI Analyst & Data Scientist |[LinkedIn](https://www.linkedin.com/in/rjbuleje/) |
| <img src="https://media.licdn.com/dms/image/v2/D4E03AQHzUlyu-XxMQw/profile-displayphoto-shrink_800_800/B4EZZjfl2.HoAg-/0/1745425959801?e=1774483200&v=beta&t=7EOOznnRQLFnGekJiMuMGUa67wzv0AFNuJajDJK7phk" width="60" alt="Giancarlo" style="border-radius: 50%;" /> | Giancarlo Poémape| Data Engineer & ML Engineer |[LinkedIn](https://www.linkedin.com/in/giancarlopoemape/) |

