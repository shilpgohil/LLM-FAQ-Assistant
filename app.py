{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   #"id": "8acd3f9f-b5c8-40f8-8944-f9778e9fd1cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: flask in c:\\users\\shilp\\anaconda3\\lib\\site-packages (3.0.3)\n",
      "Requirement already satisfied: openai in c:\\users\\shilp\\anaconda3\\lib\\site-packages (1.60.2)\n",
      "Requirement already satisfied: Werkzeug>=3.0.0 in c:\\users\\shilp\\anaconda3\\lib\\site-packages (from flask) (3.0.3)\n",
      "Requirement already satisfied: Jinja2>=3.1.2 in c:\\users\\shilp\\anaconda3\\lib\\site-packages (from flask) (3.1.4)\n",
      "Requirement already satisfied: itsdangerous>=2.1.2 in c:\\users\\shilp\\anaconda3\\lib\\site-packages (from flask) (2.2.0)\n",
      "Requirement already satisfied: click>=8.1.3 in c:\\users\\shilp\\anaconda3\\lib\\site-packages (from flask) (8.1.7)\n",
      "Requirement already satisfied: blinker>=1.6.2 in c:\\users\\shilp\\anaconda3\\lib\\site-packages (from flask) (1.6.2)\n",
      "Requirement already satisfied: anyio<5,>=3.5.0 in c:\\users\\shilp\\anaconda3\\lib\\site-packages (from openai) (4.2.0)\n",
      "Requirement already satisfied: distro<2,>=1.7.0 in c:\\users\\shilp\\anaconda3\\lib\\site-packages (from openai) (1.9.0)\n",
      "Requirement already satisfied: httpx<1,>=0.23.0 in c:\\users\\shilp\\anaconda3\\lib\\site-packages (from openai) (0.27.0)\n",
      "Requirement already satisfied: jiter<1,>=0.4.0 in c:\\users\\shilp\\anaconda3\\lib\\site-packages (from openai) (0.8.2)\n",
      "Requirement already satisfied: pydantic<3,>=1.9.0 in c:\\users\\shilp\\anaconda3\\lib\\site-packages (from openai) (2.5.3)\n",
      "Requirement already satisfied: sniffio in c:\\users\\shilp\\anaconda3\\lib\\site-packages (from openai) (1.3.0)\n",
      "Requirement already satisfied: tqdm>4 in c:\\users\\shilp\\anaconda3\\lib\\site-packages (from openai) (4.66.4)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.11 in c:\\users\\shilp\\anaconda3\\lib\\site-packages (from openai) (4.11.0)\n",
      "Requirement already satisfied: idna>=2.8 in c:\\users\\shilp\\anaconda3\\lib\\site-packages (from anyio<5,>=3.5.0->openai) (3.7)\n",
      "Requirement already satisfied: colorama in c:\\users\\shilp\\anaconda3\\lib\\site-packages (from click>=8.1.3->flask) (0.4.6)\n",
      "Requirement already satisfied: certifi in c:\\users\\shilp\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->openai) (2024.8.30)\n",
      "Requirement already satisfied: httpcore==1.* in c:\\users\\shilp\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->openai) (1.0.2)\n",
      "Requirement already satisfied: h11<0.15,>=0.13 in c:\\users\\shilp\\anaconda3\\lib\\site-packages (from httpcore==1.*->httpx<1,>=0.23.0->openai) (0.14.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\shilp\\anaconda3\\lib\\site-packages (from Jinja2>=3.1.2->flask) (2.1.3)\n",
      "Requirement already satisfied: annotated-types>=0.4.0 in c:\\users\\shilp\\anaconda3\\lib\\site-packages (from pydantic<3,>=1.9.0->openai) (0.6.0)\n",
      "Requirement already satisfied: pydantic-core==2.14.6 in c:\\users\\shilp\\anaconda3\\lib\\site-packages (from pydantic<3,>=1.9.0->openai) (2.14.6)\n"
     ]
    }
   ],
   "source": [
    "!pip install  flask openai"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "46d515bb-a2f3-412d-a718-045af38d450f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import openai\n",
    "from flask import Flask, request, render_template\n",
    "from config import get_config  # Import the function to fetch API key\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Load OpenAI API key from config.json\n",
    "config = get_config()\n",
    "openai.api_key = config.get(\"openai_api_key\", \"\")\n",
    "\n",
    "if not openai.api_key:\n",
    "    raise ValueError(\"OpenAI API key not found in config.json\")\n",
    "\n",
    "# Load Knowledge Base\n",
    "def load_knowledge_base():\n",
    "    with open(\"data/knowledge_base.json\", \"r\", encoding=\"utf-8\") as f:\n",
    "        return json.load(f)\n",
    "\n",
    "knowledge_base = load_knowledge_base()\n",
    "\n",
    "# Function to get response from OpenAI\n",
    "def get_openai_response(query):\n",
    "    try:\n",
    "        response = openai.ChatCompletion.create(\n",
    "            model=\"gpt-3.5-turbo\",\n",
    "            messages=[\n",
    "                {\"role\": \"system\", \"content\": \"You are a helpful FAQ assistant.\"},\n",
    "                {\"role\": \"user\", \"content\": query}\n",
    "            ]\n",
    "        )\n",
    "        return response[\"choices\"][0][\"message\"][\"content\"]\n",
    "    except Exception as e:\n",
    "        return f\"Error: {str(e)}\"\n",
    "\n",
    "@app.route(\"/\")\n",
    "def index():\n",
    "    return render_template(\"index.html\")\n",
    "\n",
    "@app.route(\"/ask\", methods=[\"POST\"])\n",
    "def ask():\n",
    "    user_query = request.form.get(\"query\", \"\")\n",
    "    \n",
    "    if not user_query:\n",
    "        return {\"answer\": \"Please enter a valid query.\"}, 400\n",
    "    \n",
    "    # Check if answer is in knowledge base\n",
    "    answer = knowledge_base.get(user_query.lower())\n",
    "    \n",
    "    if not answer:\n",
    "        answer = get_openai_response(user_query)  # Use OpenAI if not in KB\n",
    "    \n",
    "    return {\"answer\": answer}\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
