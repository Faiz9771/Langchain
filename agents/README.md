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

# AutoSQLRep - Automated SQL Reporting Agent

## Overview
AutoSQLRep is an intelligent SQL reporting agent built with LangChain and Google's Gemini AI that automatically generates insights from your database using natural language queries. Simply ask questions in plain English, and the agent will translate them into SQL queries and provide meaningful answers.

## Features
- 🤖 **Natural Language to SQL**: Ask questions in plain English
- 🔍 **Intelligent Query Generation**: Automatically generates optimized SQL queries
- 📊 **Real-time Database Insights**: Get instant answers from your data
- 🛡️ **Safe Query Execution**: Built-in safeguards against harmful operations
- 🔧 **Multiple Database Support**: Works with MySQL, PostgreSQL, SQLite, and more

## Prerequisites
- Python 3.11+
- MySQL Server running locally
- Google API Key for Gemini AI
- Required Python packages (see requirements.txt)

db = SQLDatabase.from_uri("mysql+mysqlconnector://root:password@localhost:3306/Langchain")

