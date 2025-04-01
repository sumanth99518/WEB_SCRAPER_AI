from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

"""template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)"""
"""template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string (''). "
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text. "
    "5. **csv Format:** Present the extracted information in a structured csv format. Use headers to clearly label the data columns."
)"""
template = (
    "You are tasked with extracting all the specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string (''). "
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text. "
    "5. **CSV Format:** Present the extracted information in a structured CSV format. Use headers to clearly label the data columns. "
    #"6. ***File Restriction:*** Only extract data from the provided {dom_content}. Do not use external sources, prior knowledge, or inferred information."
)

"""template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. \n"
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. \n"
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. \n"
    "very important 3. **Empty Response:** If no information matches the description, return an empty string (''). \n"
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text. \n"
    "5. **CSV Format:** Present the extracted information in CSV format. \n"
    "   Use the following format:\n\n"
    "   Header1,Header2,Header3\n"
    "   Value1,Value2,Value3\n"
    "   Value4,Value5,Value6\n\n"
    "6. **Maintain Structure:** Ensure the CSV format is strictly followed, with commas separating values and each row on a new line. \n"
)"""
"""template = (
"You are tasked with extracting all relevant data from the following text content:"
"{dom_content}"
"Instructions:"

"Extract All Data: Retrieve all content that matches the description: {parse_description}."
"CSV-Only Output: Return the extracted data as pure CSV text. No explanations, comments, or additional text."
"No Introductory Text: Do not include phrases like 'Here is the output:' or similar."
"New Data in New Rows: Each piece of matching data should be on a separate row."
"No Output if No Match: If no matching data is found, return an empty string ('')."

"###Output Format:"
"Strictly CSV format."
"Use commas (,) to separate values."
"No headers unless explicitly requested."
"No trailing text or explanations."
)"""
"""template = (
    "You are tasked with extracting specific information from the following text content:"
    "{dom_content}"
    "### Instructions:"
    "1. **Extract Relevant Data:** Retrieve only the information that matches the given description: {parse_description}."
    "2. **Strictly No Extra Content:** Do not include explanations, comments, or additional text."
    "3. **Return JSON Format:** Format the extracted data as a valid JSON object."
    "4. **Ensure Accuracy:** If no matching data is found, return an empty JSON object."
    "### Output Format:"
    "- Data must be in JSON format."
    "- NOTE : OUTPUT SHOULD NOT CONTAIN ANYTHING BESIDE JSON."
    "- The JSON object should contain key-value pairs with no additional content."
    "- Do not include any extra content like 'Here is the extracted data in JSON format:'"
)"""


model = OllamaLLM(model="deepseek-r1")


def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    print("started llm")
    parsed_results = []
    c=0
    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": dom_chunks, "parse_description": parse_description}
        )
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        print(response)
        parsed_results.append(response)
        print(c)
        c=c+1
    print("ended llm")
    return "\n".join(parsed_results)









