# Conversational-AI-demo

## Overview

This system employs three specialized agents that work together to provide comprehensive customer service:

1. **TriageAgent** - The initial point of contact that identifies customers and routes them to the appropriate department
2. **SalesAgent** - Assists customers with product selection and order placement
3. **ReturnsAgent** - Handles return requests and provides order history information

## Features

- **Multi-Agent Architecture**: Seamless transfer between specialized agents with context preservation
- **Customer Identification**: Persistent customer database tracks shoppers and their order history
- **Context Preservation**: Conversation history transfers between agents for continuity
- **Order Management**: Complete order workflow from item selection to checkout
- **Return Processing**: Access order history and process returns with reasons
- **Voice-Enabled**: Built using LiveKit's voice capabilities with support for:
  - Speech-to-Text (STT) using Deepgram
  - Large Language Model (LLM) using Google Gemini
  - Text-to-Speech (TTS) using Deepgram
  - Voice Activity Detection (VAD) using Silero
- **SQLite Database**: Persistent storage for customers and orders

## How It Works

1. Customer connects and is greeted by the Triage agent
2. Triage agent asks for the customer's name and identifies them in the system
3. Based on the customer's needs, they are transferred to either:
   - Sales agent for making purchases
   - Returns agent for processing returns
4. Agents can transfer customers between departments as needed
5. All customer information and order history persists across sessions
6. Context and conversation history follows the customer between agents

. Create a `.env` file with your API credentials:
   ```
   LIVEKIT_URL=your_livekit_url
   LIVEKIT_API_KEY=your_api_key
   LIVEKIT_API_SECRET=your_api_secret
   GOOGLE_API_KEY=your_api_key
   DEEPGRAM_API_KEY=your_deepgram_key
   ```

## Running the Agent

```bash
python personal_shopper.py console
