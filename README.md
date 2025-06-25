# Gemini AI Hyperparameter Playground

![Project Banner](https://img.shields.io/badge/Gemini%20AI-Hyperparameter%20Playground-blue?style=for-the-badge&logo=google&logoColor=white)

## 📋 Project Overview

This interactive Streamlit application allows users to experiment with Google's Gemini AI models by adjusting various hyperparameters and seeing in real-time how these changes affect the model's responses. Perfect for AI enthusiasts, developers, prompt engineers, and anyone looking to understand how AI language models work "under the hood."

### 🎯 Purpose

The purpose of this application is to:
- Provide an educational tool for understanding AI model parameters
- Allow experimentation with different Gemini models and settings
- Demonstrate how hyperparameter tuning affects AI outputs
- Help users optimize prompts and settings for their specific needs

### 🛠️ Built With
- ![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)
- ![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red?style=flat&logo=streamlit)
- ![Google Generative AI](https://img.shields.io/badge/Google%20Generative%20AI-API-green?style=flat&logo=google)

## 🌟 Features

### Sidebar Controls:
- **Hyperparameter Adjustment:**
  - Temperature: Control randomness and creativity
  - Top-p (Nucleus Sampling): Control diversity of responses
  - Top-k: Limit token selection to most likely options
  - Token limit: Set maximum output length
  - Stop sequence: Define custom text that ends generation
  - Frequency penalty: Reduce repetition of common tokens
  - Presence penalty: Encourage exploration of new words
- **Theme Toggle:** Switch between light and dark mode for comfortable viewing

### Main Interface:
- **API Integration:**
  - Secure API key input field with direct link to Google AI Studio
  - Support for multiple Gemini models (gemini-1.0-pro, gemini-1.5-pro, gemini-1.5-flash)
  
- **Interactive Features:**
  - Pre-loaded sample prompts for quick testing
  - Custom prompt input with spacious text area
  - One-click response generation
  - Real-time parameter summary with each response
  
- **User Experience:**
  - Responsive design that adapts to different screen sizes
  - Clear separation of input, controls, and output sections
  - Elegant styling with consistent visual language
  - Interactive expandable educational sections

- **Technical Features:**
  - Comprehensive error handling with user-friendly messages
  - Session state management for persistent settings
  - Efficient API call management
  - Custom CSS for enhanced visual appeal

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- A Google AI Studio account with API key ([Get yours here](https://aistudio.google.com/app/apikey))

### Installation Steps

1. **Clone the repository:**
   ```sh
   git clone https://github.com/arnandew-microsoft/gemini-hyperparameter-playground.git
   cd gemini-hyperparameter-playground
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```sh
   python -m venv .venv
   # On Windows
   .\.venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install streamlit google-generativeai
   ```

4. **Run the application:**
   ```sh
   streamlit run app.py
   ```

## 🎮 How to Use

1. **Start the application** by running `streamlit run app.py`
2. **Enter your Gemini API key** at the top of the main interface (get one from [Google AI Studio](https://aistudio.google.com/app/apikey))
3. **Select a Gemini model** from the dropdown menu (different models have different capabilities and performance characteristics)
4. **Set hyperparameters** using the sliders and inputs in the sidebar
5. **Enter a prompt** in the text area or select a pre-defined sample prompt
6. **Click "Generate Response"** to see the model's output
7. **Review the parameter summary** shown below each response to understand what settings were used
8. **Experiment with different settings** to see how they affect the model's responses
9. **Expand the educational section** to learn more about each hyperparameter

## 🧠 Understanding Hyperparameters

The core educational value of this application is learning how different hyperparameters affect AI model outputs. Here's what each parameter does:

### Temperature (0.0 to 1.0)
Controls randomness and creativity in the model's responses:
- **Low values (0.1-0.4)**: More deterministic, focused, and predictable responses
- **Medium values (0.5-0.7)**: Balanced between creativity and coherence
- **High values (0.7-1.0)**: More creative, diverse, and sometimes surprising responses

*Best for*: Lower for factual tasks, higher for creative writing

### Top-p / Nucleus Sampling (0.0 to 1.0)
Controls diversity by considering the smallest set of tokens whose cumulative probability exceeds the set value:
- **Low values (0.1-0.4)**: Considers only the most likely tokens, resulting in more focused text
- **Medium values (0.5-0.7)**: Balanced consideration of likely tokens
- **High values (0.7-0.9)**: Considers a wider range of tokens, introducing more diversity

*Best for*: Lower for precision tasks, higher for exploratory content

### Top-k (1 to 100)
Limits token selection to the top k most likely tokens at each step:
- **Low values (1-10)**: Very limited selection, more predictable output
- **Medium values (20-40)**: Balanced token selection
- **High values (50+)**: Wider range of token options, potentially more varied output

*Best for*: Lower for specific, controlled output, higher for creative tasks

### Token Limit (50 to 8192)
Sets the maximum length of the generated response in tokens (roughly 4 characters or 0.75 words per token):
- Shorter limits are useful for concise answers
- Longer limits allow for detailed explanations, stories, or code generation

*Best for*: Adjust based on how much content you want the model to generate

### Stop Sequences
Custom text patterns that will cause the model to stop generating when encountered:
- Useful for controlling output format
- Can specify multiple stop sequences (one per line)
- Common examples: "\n\n", "###", "END"

*Best for*: Creating structured outputs or preventing the model from continuing beyond a certain point

### Frequency Penalty (0.0 to 2.0)
Reduces repetition by penalizing tokens based on their frequency in the text so far:
- **0.0**: No penalty for repetition
- **0.5 - 1.0**: Moderate discouragement of repetition
- **1.5 - 2.0**: Strong discouragement of repetition

*Best for*: Reducing repetitive phrases or patterns in longer content

### Presence Penalty (0.0 to 2.0)
Reduces repetition by penalizing tokens that have appeared at all in the text so far:
- **0.0**: No penalty for using the same tokens again
- **0.5 - 1.0**: Moderate encouragement of new tokens
- **1.5 - 2.0**: Strong encouragement to use new tokens and concepts

*Best for*: Encouraging the model to explore new topics, ideas, or vocabulary

## 📸 Application Screenshots

### Main Interface
![Main interface of Gemini AI Hyperparameter Playground](./screenshots/main-interface.png)
*The main interface showing the API key input, model selection dropdown, prompt area, and response section.*

### Hyperparameter Controls
![Sidebar with hyperparameter controls](./screenshots/hyperparameter-controls.png)
*The sidebar with sliders for adjusting temperature, top-p, top-k, token limit, and other hyperparameters.*

### Response Generation
![Response generation example](./screenshots/response-example.png)
*An example of a generated response showing the model output and a detailed parameter summary below.*

### Educational Section
![Hyperparameter explanation section](./screenshots/educational-section.png)
*The expandable educational section explaining how each hyperparameter affects model behavior.*

## 📊 Application Structure

The application is structured as follows:

```
gemini-hyperparameter-playground/
│
├── app.py                # Main Streamlit application file
├── README.md             # Project documentation
├── .gitignore            # Git ignore file
│
└── screenshots/          # Application screenshots
    ├── main-interface.png
    ├── hyperparameter-controls.png
    ├── response-example.png
    └── educational-section.png
```

## 📋 Code Highlights

The application is built with clean, modular code that demonstrates several key Streamlit and Gemini API concepts:

- **State Management**: Using `st.session_state` for preserving user inputs
- **Custom Styling**: CSS enhancements for better user experience
- **Error Handling**: Graceful error handling for API issues
- **Responsive Layout**: Using Streamlit's layout options for an intuitive interface
- **Parameter Configuration**: Properly formatting parameters for the Gemini API

## 🔮 Future Enhancements

Possible future improvements:

- Add ability to export/import parameter presets
- Implement side-by-side comparison of different parameter settings
- Add visualization of how parameter changes affect response metrics
- Support for more Gemini models as they are released
- User authentication to save personal API keys securely

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## ✨ Taking Screenshots for the README

To properly document the application, take screenshots of the following:

1. **Main Interface** (`main-interface.png`): Capture the full application showing API key input, model selection, and prompt area
2. **Hyperparameter Controls** (`hyperparameter-controls.png`): Take a screenshot of the sidebar with all the sliders
3. **Response Generation** (`response-example.png`): Show an example response with parameter summary below it
4. **Educational Section** (`educational-section.png`): Capture the expanded "Learn About Hyperparameters" section

Save these screenshots to the `/screenshots` directory to automatically include them in the README.

---

**Happy experimenting with Gemini AI Hyperparameters!** 🚀
