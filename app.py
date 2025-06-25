import streamlit as st
import google.generativeai as genai
import json
from datetime import datetime

# App title and configuration
st.set_page_config(
    page_title="Gemini AI Hyperparameter Playground",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for light and dark themes
def apply_custom_css():
    st.markdown("""
        <style>
        /* Common styles */
        .parameter-heading {
            font-size: 1.2rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        .parameter-description {
            margin-bottom: 1rem;
            font-size: 0.9rem;
        }
        .response-container {
            padding: 1.5rem;
            margin-top: 1rem;
            border-radius: 10px;
        }
        .param-summary {
            padding: 1rem;
            border-radius: 8px;
            margin-top: 1rem;
        }
        .app-header {
            text-align: center; 
            margin-bottom: 1rem;
        }
        
        /* Light theme */
        .light-theme .response-container {
            background-color: #f0f2f6;
            border: 1px solid #ddd;
        }
        .light-theme .param-summary {
            background-color: #e6f3ff;
            border: 1px solid #b3d7ff;
        }
        
        /* Dark theme */
        .dark-theme .response-container {
            background-color: #1e1e1e;
            border: 1px solid #333;
        }
        .dark-theme .param-summary {
            background-color: #2d2d2d;
            border: 1px solid #444;
        }
        </style>
        """, unsafe_allow_html=True)

apply_custom_css()

# Initialize session state variables
if 'api_key' not in st.session_state:
    st.session_state.api_key = ""
if 'theme' not in st.session_state:
    st.session_state.theme = "light"
if 'response' not in st.session_state:
    st.session_state.response = ""
if 'parameters_used' not in st.session_state:
    st.session_state.parameters_used = {}
if 'response_time' not in st.session_state:
    st.session_state.response_time = ""
if 'error_message' not in st.session_state:
    st.session_state.error_message = ""

# Theme switcher in sidebar
def toggle_theme():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

# Apply the selected theme class
theme_class = "light-theme" if st.session_state.theme == "light" else "dark-theme"
st.markdown(f'<div class="{theme_class}">', unsafe_allow_html=True)

# Sidebar for hyperparameters
with st.sidebar:
    st.title("Hyperparameter Controls")
    
    # Theme toggle
    theme_label = "🌙 Dark Mode" if st.session_state.theme == "light" else "☀️ Light Mode"
    st.button(theme_label, on_click=toggle_theme)
    
    st.divider()
    
    # Hyperparameters
    st.subheader("Model Parameters")
    
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Controls randomness. Lower values make responses more focused and deterministic, higher values make responses more creative and varied."
    )
    
    top_p = st.slider(
        "Top-p (Nucleus Sampling)",
        min_value=0.0,
        max_value=1.0,
        value=0.9,
        step=0.1,
        help="Controls diversity by considering tokens with top_p probability mass. Lower values make responses more focused, higher values introduce more diversity."
    )
    
    top_k = st.slider(
        "Top-k",
        min_value=1,
        max_value=100,
        value=40,
        step=1,
        help="Limits token selection to the top k most likely tokens. Lower values generate more predictable text, higher values allow more variety."
    )
    
    max_tokens = st.slider(
        "Maximum Output Tokens",
        min_value=50,
        max_value=8192,
        value=1024,
        step=50,
        help="Maximum number of tokens to generate in the response."
    )
    
    stop_sequences = st.text_area(
        "Stop Sequences (one per line)",
        height=100,
        help="Sequences that will stop generation when encountered. Enter one per line."
    )
    
    frequency_penalty = st.slider(
        "Frequency Penalty",
        min_value=0.0,
        max_value=2.0,
        value=0.0,
        step=0.1,
        help="Reduces repetition by penalizing tokens based on their frequency in the text so far."
    )
    
    presence_penalty = st.slider(
        "Presence Penalty",
        min_value=0.0,
        max_value=2.0,
        value=0.0,
        step=0.1,
        help="Reduces repetition by penalizing tokens that have appeared at all in the text so far."
    )

# Main content area
st.markdown('<h1 class="app-header">🧪 Gemini AI Hyperparameter Playground</h1>', unsafe_allow_html=True)
st.write("Experiment with different hyperparameters to see how they affect Gemini's responses.")

# API key input
api_key = st.text_input(
    "Enter your Gemini API Key",
    type="password",
    value=st.session_state.api_key if st.session_state.api_key else "",
    help="Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)"
)

if api_key:
    st.session_state.api_key = api_key
    genai.configure(api_key=api_key)

# Model selection
available_models = [
    "gemini-1.0-pro", 
    "gemini-1.5-pro", 
    "gemini-1.5-flash"
]

selected_model = st.selectbox("Select Gemini Model", available_models)

# Sample prompts
sample_prompts = {
    "Create your own prompt": "",
    "Creative Writing": "Write a short story about an AI that learns to feel emotions.",
    "Factual Query": "Explain how transformer neural networks work in simple terms.",
    "Code Generation": "Write a Python function that takes a list of numbers and returns the median value.",
    "Problem Solving": "I need to organize a team dinner for 12 people with various dietary restrictions. How should I approach this?",
    "Reasoning Task": "If it takes 5 machines 5 minutes to make 5 widgets, how long would it take 100 machines to make 100 widgets?"
}

selected_prompt_key = st.selectbox("Sample Prompts", list(sample_prompts.keys()))

if selected_prompt_key == "Create your own prompt":
    user_prompt = st.text_area("Enter your prompt", height=150)
else:
    user_prompt = st.text_area("Enter your prompt", value=sample_prompts[selected_prompt_key], height=150)

# Process stop sequences
stop_seq_list = [seq.strip() for seq in stop_sequences.split('\n') if seq.strip()] if stop_sequences else None

# Generate response
if st.button("Generate Response", type="primary", disabled=not (api_key and user_prompt)):
    with st.spinner("Generating response..."):
        try:
            st.session_state.error_message = ""
            
            # Configure the model
            generation_config = {
                "temperature": temperature,
                "top_p": top_p,
                "top_k": top_k,
                "max_output_tokens": max_tokens,
                "stop_sequences": stop_seq_list,
            }
            
            # Store parameters for display
            st.session_state.parameters_used = {
                "model": selected_model,
                "temperature": temperature,
                "top_p": top_p,
                "top_k": top_k,
                "max_output_tokens": max_tokens,
                "stop_sequences": stop_seq_list if stop_seq_list else "None",
                "frequency_penalty": frequency_penalty,
                "presence_penalty": presence_penalty
            }
            
            # Initialize the model
            model = genai.GenerativeModel(
                model_name=selected_model,
                generation_config=generation_config
            )
            
            # Record start time
            start_time = datetime.now()
            
            # Generate content
            response = model.generate_content(user_prompt)
            
            # Record time taken
            end_time = datetime.now()
            time_taken = (end_time - start_time).total_seconds()
            st.session_state.response_time = f"{time_taken:.2f} seconds"
            
            # Store response
            st.session_state.response = response.text
            
        except Exception as e:
            st.session_state.error_message = str(e)
            st.session_state.response = ""

# Display the response
if st.session_state.response:
    st.subheader("Generated Response")
    st.markdown(f'<div class="response-container">{st.session_state.response}</div>', unsafe_allow_html=True)
    
    st.subheader("Parameters Summary")
    params_md = "\n".join([f"**{k}:** {v}" for k, v in st.session_state.parameters_used.items()])
    st.markdown(f'<div class="param-summary">{params_md}</div>', unsafe_allow_html=True)
    st.write(f"Response generated in {st.session_state.response_time}")

# Display any errors
if st.session_state.error_message:
    st.error(f"Error: {st.session_state.error_message}")

# Educational section about hyperparameters
with st.expander("Learn About Hyperparameters"):
    st.subheader("Understanding LLM Hyperparameters")
    
    st.markdown("""
    ### Temperature (0.0 to 1.0)
    Controls randomness in token selection. Lower values make responses more deterministic and focused, while higher values introduce more randomness and creativity.
    
    - **Low (0.1 - 0.4)**: More deterministic, factual, and consistent responses
    - **Medium (0.5 - 0.7)**: Balanced between creativity and coherence
    - **High (0.8 - 1.0)**: More creative, diverse, and unpredictable responses
    
    ### Top-p / Nucleus Sampling (0.0 to 1.0)
    Controls diversity by considering the smallest set of tokens whose cumulative probability exceeds top_p.
    
    - **Low (0.1 - 0.4)**: Considers only the most likely tokens, resulting in more focused text
    - **Medium (0.5 - 0.7)**: Balanced consideration of likely tokens
    - **High (0.8 - 0.95)**: Considers a wider range of tokens, introducing more diversity
    
    ### Top-k (1 to 100)
    Limits token selection to the top k most likely tokens.
    
    - **Low (1 - 10)**: Very limited selection, more predictable output
    - **Medium (20 - 40)**: Balanced token selection
    - **High (50+)**: Wider range of token options, potentially more varied output
    
    ### Maximum Output Tokens
    The maximum number of tokens to generate in the response. A token is roughly 4 characters or 0.75 words.
    
    ### Stop Sequences
    Specific strings that will cause the model to stop generating when encountered. Useful for formatting or controlling output structure.
    
    ### Frequency Penalty (0.0 to 2.0)
    Penalizes tokens based on their frequency in the text so far. Higher values reduce repetition.
    
    - **0.0**: No penalty for repetition
    - **0.5 - 1.0**: Moderate discouragement of repetition
    - **1.5 - 2.0**: Strong discouragement of repetition
    
    ### Presence Penalty (0.0 to 2.0)
    Penalizes tokens that have appeared at all in the text so far, regardless of frequency.
    
    - **0.0**: No penalty for using the same tokens again
    - **0.5 - 1.0**: Moderate encouragement of new tokens
    - **1.5 - 2.0**: Strong encouragement to use new tokens and concepts
    """)

# Additional information
st.divider()
st.caption("This app is for educational purposes. Created to help understand how different hyperparameters affect LLM outputs.")

# Close the theme div
st.markdown('</div>', unsafe_allow_html=True)
