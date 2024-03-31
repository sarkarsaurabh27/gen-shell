#!/usr/bin/env python3
import json
import logging
import platform
import subprocess
import sys
import warnings

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from pydantic import BaseModel, Field
from urllib3.exceptions import InsecureRequestWarning

# Load environment variables from a .env file
load_dotenv()

log = logging.getLogger(__name__)


class RegenerationLLMOutputModel(BaseModel):
    command: str = Field(description="Command to run for the task.")
    installation: str = Field(description="Command to install the tool, in case.")
    check: str = Field(description="Command to check if the tool is installed or not.")
    link: str = Field(description="Online link to find more about the command/tool.")


class GenShellAgent:
    def __init__(self) -> None:
        self.llm = ChatOpenAI(model_name="gpt-4-turbo-preview", temperature=0.0)
        self.parser = JsonOutputParser(pydantic_object=RegenerationLLMOutputModel)
        self.prompt = PromptTemplate(input_variables=['task', 'platform'],
                                     partial_variables={
                                                    "format_instructions": self.parser.get_format_instructions()},
                                     template="""
                                              You are a bash expert that can help recommend correct command based on the provided input task.
                                              Always provide optional install command for the tool.

                                              Task: {task}
                                              Platform: {platform}

                                              If you cannot find the command, respond with any online link to look for.

                                              {format_instructions}
                                              """)


    def run(self, task: str):
        chain = self.prompt | self.llm | self.parser
        os_info = platform.platform()
        try:
            response = chain.invoke(input={"task": task, "platform": os_info})
        except OutputParserException as ope:
            log.error("Output parser error path")
            secondary_parse_attempt(ope.llm_output)
        return response


def secondary_parse_attempt(response_text):
    import re
    # Try to find JSON string within triple backticks
    def parse_json(response_text):
        match = re.search(r"```json()?(.*)", response_text, re.DOTALL)

        # If no match found, assume the entire string is a JSON string
        if match is None:
            json_str = response_text
        else:
            # If match found, use the content within the backticks
            json_str = match.group(2)
        # Strip whitespace and newlines from the start and end
        json_str = json_str.strip().strip("`")
        return json.loads(json_str)

    try:
        return parse_json(response_text)
    except Exception as e:
        return {'command': response_text, 'installation': None, 'check': None, 'link': None}


def main():
    """
    Main function to run the CLI tool.
    """
    if len(sys.argv) != 2:
        print("Usage: gen-shell 'task description'")
        sys.exit(1)

    task_description = " ".join(sys.argv[1:])
    gen_shell_agent = GenShellAgent()
    command = gen_shell_agent.run(task_description)
    log.debug (command)
    if command['link']:
        print ("Learn More: " + command['link'])
    if command['check']:
        # Run the command and capture the output
        result = subprocess.run(command['check'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Check if the command was successful
        if result.returncode == 1 and command['installation']:
            print ("Required tooling not available on this machine.")
            user_input = input(f"Run Command: `{command['check']}`? (Y/n): ")
            # Normalize the input to lowercase to make the check case-insensitive
            user_input = user_input.lower()
            if user_input in ['yes', 'y']:
                subprocess.run(command['installation'], shell=True, text=True)
            else:
                sys.exit(0)
    if command['command']:
        user_input = input(f"Run Command: `{command['command']}`? (Y/n): ")
        # Normalize the input to lowercase to make the check case-insensitive
        user_input = user_input.lower()
        if user_input in ['yes', 'y']:
            subprocess.run(command['command'], shell=True, text=True)

if __name__ == "__main__":
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=InsecureRequestWarning)
        main()
