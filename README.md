# Lead Email Generator

This Streamlit app processes a CSV file containing lead information and generates personalized emails using two different Language Models (LLMs): OpenAI's GPT-3.5-turbo and an opensource GPT-2 from `transformers`. The app compares the outputs from both LLMs and determines which one is better for sending.

## Features

- CSV file upload and parsing
- Email generation using OpenAI and Anthropic APIs
- Simple comparison of generated emails
- JSON storage of results
- Progress bar for processing leads
- Display of sample results

## Requirements

- Python 3.7+
- Streamlit
- Pandas
- OpenAI Python library
- Anthropic Python library

## Installation

1. Clone this repository:
```
git clone https://github.com/yourusername/lead-email-generator.git
cd lead-email-generator
```

2. Install the required packages:

```pip install -r requirements.txt```

3. Set up your API keys:
- Create a `.env` file in the project root
- Add your API keys to the `.env` file:
  ```
  `OPENAI_API_KEY``=your-openai-api-key
  ```

## Usage

1. Run the Streamlit app:
`streamlit run app.py`

2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Upload a CSV file containing lead information. The CSV should have the following columns:
- name
- email
- company
- job_title

4. The app will process the leads and generate emails using both LLMs.

5. Results will be saved to `output.json` in the project directory.

6. Sample results will be displayed in the app.

## Approach

1. **Data Extraction**: The app uses Pandas to read and parse the uploaded CSV file.

2. **Email Generation**: Two functions, `generate_email_openai()` and `generate_email_gpt2()`, use the respective APIs to generate personalized emails based on lead information.

3. **Comparison**: A simple comparison function, `compare_emails()`, determines which email is "better" based on length. In a real-world scenario, this would be replaced with a more sophisticated comparison method.

4. **Storage**: Results are stored in a JSON file using the `save_to_json()` function.

5. **User Interface**: Streamlit is used to create a simple web interface for file upload and result display.

## Time spent
1h 20 min

## Future Improvements

- Implement more sophisticated email comparison methods
- Add error handling and input validation
- Integrate with email sending services
- Implement MORL for optimizing email content
- Add user authentication and rate limiting

## License

This project is licensed under the MIT License.