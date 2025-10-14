# 🔬 Research Agent

A comprehensive AI-powered research assistant built with LangChain that combines multiple information sources to provide deep, well-researched answers to complex questions.

## 🚀 Features

### **Multi-Source Research Capabilities**
- **Wikipedia Integration**: Access to general knowledge and overview information
- **Enhanced Arxiv Search**: Academic papers and research with detailed content (5 results, 2000 chars each)
- **Intelligent Tool Selection**: Automatically chooses the best research tools for each query
- **Comprehensive Analysis**: Combines information from multiple sources for complete understanding

### **Advanced Research Methodology**
- **Structured Analysis**: Provides executive summaries, detailed analysis, key findings, and source citations
- **Trend Analysis**: Identifies patterns and connections between sources
- **Gap Identification**: Suggests further research directions
- **Configurable Depth**: Supports shallow, medium, and deep analysis levels

### **Jupyter-Compatible Interface**
- **Interactive Widgets**: Real-time chat interface with text input and buttons
- **Conversation History**: Tracks and displays chat history
- **Error Handling**: Robust error management and user feedback
- **Multiple Interaction Methods**: Widget-based, function-based, and batch processing

## 🛠️ Technical Stack

- **Language Model**: Google Gemini 2.0 Flash
- **Framework**: LangChain
- **Tools**: Wikipedia API, Arxiv API
- **Interface**: Jupyter Widgets (ipywidgets)
- **Environment**: Python 3.11+

## 📋 Prerequisites

### **Required Packages**
```bash
pip install langchain
pip install langchain-community
pip install langchain-google-genai
pip install ipywidgets
pip install python-dotenv
pip install arxiv
pip install wikipedia
```

### **Environment Setup**
1. Create a `.env` file in your project root
2. Add your Google API key:
```env
GOOGLE_API_KEY=your_google_api_key_here
```

## 🚀 Quick Start

### **1. Setup Environment**
```python
from dotenv import load_dotenv
load_dotenv()
import os
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
```

### **2. Initialize Research Agent**
```python
# The agent is automatically created when you run the notebook
# It includes Wikipedia and Arxiv tools with enhanced configurations
```

### **3. Start Interactive Chat**
```python
# Run the Jupyter chat interface
jupyter_chat = JupyterChat(agent_executor)
```

## 🔧 Configuration

### **Arxiv Search Settings**
- **Results**: 5 papers per query
- **Content Length**: 2000 characters per paper
- **Max Documents**: 10 documents loaded
- **Error Handling**: Continues on failure

### **Wikipedia Settings**
- **Results**: 1 result per query
- **Content Length**: 200 characters
- **Language**: English

### **Agent Configuration**
- **Max Iterations**: 5
- **Temperature**: 0 (deterministic responses)
- **Verbose**: True (shows tool usage)

## 📊 Usage Examples

### **Research Questions**
```python
# Academic Research
"What are the latest developments in transformer architecture?"

# General Knowledge
"What is quantum computing?"

# Comparative Analysis
"Compare different approaches to natural language processing"

# Trend Analysis
"What are the current trends in machine learning research?"
```

### **Response Structure**
The agent provides structured responses with:
1. **Executive Summary** (2-3 sentences)
2. **Detailed Analysis** (with sources)
3. **Key Findings and Insights**
4. **Current Trends and Developments**
5. **Research Gaps and Future Directions**
6. **Source Citations**

## 🎯 Research Methodology

### **Analysis Depth Levels**
- **Shallow**: Quick overview (3 sources, 1000 chars)
- **Medium**: Standard analysis (5 sources, 2000 chars)
- **Deep**: Comprehensive research (10 sources, 3000 chars)

### **Research Process**
1. **Tool Selection**: Agent analyzes query and selects appropriate tools
2. **Information Gathering**: Searches multiple sources simultaneously
3. **Synthesis**: Combines information from different sources
4. **Analysis**: Identifies patterns, trends, and connections
5. **Structured Response**: Provides comprehensive, well-cited answer

## 🔍 Available Tools

| Tool | Purpose | Configuration |
|------|---------|---------------|
| **Wikipedia** | General knowledge and overviews | 1 result, 200 chars |
| **Arxiv** | Academic papers and research | 5 results, 2000 chars |
| **Research Analysis** | Multi-source comprehensive analysis | Configurable depth |

## 🎨 Interface Features

### **Jupyter Widgets**
- **Text Input**: Type questions with placeholder text
- **Send Button**: Submit questions with click or Enter key
- **Clear Chat**: Reset conversation history
- **Exit Chat**: End session with summary

### **Chat Features**
- **Real-time Processing**: Shows "Thinking..." status
- **Error Handling**: Graceful error messages
- **Conversation Tracking**: Message counter and history
- **Input Validation**: Prevents empty submissions

## 📈 Performance & Limitations

### **Strengths**
- ✅ Multi-source information synthesis
- ✅ Academic and general knowledge access
- ✅ Structured, well-cited responses
- ✅ Jupyter-native interface
- ✅ Configurable research depth

### **Limitations**
- ⚠️ Dependent on API availability
- ⚠️ Limited to Wikipedia and Arxiv sources
- ⚠️ Response quality depends on query specificity
- ⚠️ Requires internet connection

## 🔧 Customization

### **Adding New Tools**
```python
# Add new research tools to the tools list
from langchain_community.tools import YourNewTool
new_tool = YourNewTool()
tools.append(new_tool)
```

### **Modifying Agent Prompt**
```python
# Customize the system prompt for different research styles
agent_prompt = ChatPromptTemplate.from_messages([
    ("system", "Your custom research methodology..."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])
```

### **Adjusting Tool Parameters**
```python
# Modify Arxiv settings
arxiv_wrapper = ArxivAPIWrapper(
    top_k_results=10,  # More results
    doc_content_chars_max=5000,  # Longer content
    load_max_docs=20,  # More documents
    continue_on_failure=True
)
```

## 🐛 Troubleshooting

### **Common Issues**
1. **API Key Error**: Ensure GOOGLE_API_KEY is set in .env file
2. **Widget Not Displaying**: Install ipywidgets: `pip install ipywidgets`
3. **Import Errors**: Install missing packages from requirements
4. **Network Issues**: Check internet connection for API calls

### **Debug Mode**
```python
# Enable verbose mode for debugging
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    max_iterations=5, 
    verbose=True  # Shows tool usage
)
```

## 📚 Dependencies

- `langchain>=0.3.0`
- `langchain-community>=0.3.0`
- `langchain-google-genai>=2.0.0`
- `ipywidgets>=8.0.0`
- `python-dotenv>=1.0.0`
- `arxiv>=2.2.0`
- `wikipedia>=1.4.0`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **LangChain**: For the powerful agent framework
- **Google**: For the Gemini language model
- **Wikipedia**: For general knowledge access
- **Arxiv**: For academic research papers
- **Jupyter**: For the interactive notebook environment

---

**Built with ❤️ for researchers, students, and knowledge seekers**