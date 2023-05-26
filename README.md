# God-GPT

Welcome to **God-GPT**, a proof-of-concept repository for a godlike autonomous agent that leverages the Dalee-2 API for image creation, the GPT model for text generation, and Langchain for agent orchestration. This project provides a set of Python scripts demonstrating the capabilities of this AI framework.

For an in-depth explanation and discussion of this project, refer to this talk: [God-GPT Explained](https://www.youtube.com/live/fl1jluGawzQ?feature=share&t=454)

## Installation

Follow the instructions below to get God-GPT up and running on your local machine.

### Requirements

- Python virtual environment (venv)
- OpenAI key for GPT
- Elevenlabs key for speech synthesis

### Instructions

1. **Create a Python virtual environment (venv)**

    On the terminal, navigate to the project directory and run the following command:

    ```bash
    python3 -m venv ./venv
    ```

    Activate the virtual environment:

    ```bash
    source ./venv/bin/activate
    ```

2. **Install Dependencies**

    Ensure that you are in the project directory, then run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Setup API Keys**

    Add your OpenAI (for GPT) and Elevenlabs (for speech synthesis) keys to the .env file. Refer to the example .env file in the repository. 

    Visit the [OpenAI](https://www.openai.com/) and [Elevenlabs](https://www.elevenlabs.com/) websites to obtain your API keys if you do not already have them.

4. **Setup whisper.cpp**

    Navigate to the directory containing whisper.cpp. Follow the instructions below:

    Download the base.en model:

    ```bash
    bash ./models/download-ggml-model.sh base.en
    ```

    Build the main example and transcribe an audio file:

    ```bash
    # build the main example
    make

    # transcribe an audio file to test everything works
    ./main -f samples/jfk.wav
    ```

## Usage

To utilize the God-GPT agent, run one of the following scripts using Python:

* `talk_1.py` - Basic GPT agent
* `talk_2.py` - Agent with personality and I/O
* `talk_3.py` - Agent with personality, I/O and memory
* `talk_4.py` - Agent with  personality, I/O, memory and tools (Dalee-2)

## License

This project is licensed under the terms of the MIT License.

## Support

Are you in need of assistance with your Applied AI project? We are happy to help! Visit [Applifting.ai](https://www.applifting.ai/) for more information.
