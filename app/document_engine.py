import os
from datetime import datetime
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    model = None

def generate_document_ai(doc_type, name, position, company, start_date, end_date, salary, notes):
    """
    Generates a professional document using Gemini AI if available, 
    otherwise falls back to hardcoded professional templates.
    """
    if model and api_key:
        try:
            prompt = f"""
            You are Pooja Maru, Senior HR Director at 'Prakriti Enterprise', a premium nature-conscious organization. 
            Generate a high-end, professional, and warmly worded '{doc_type}' for the following details:
            - Recipient Name: {name}
            - Position: {position}
            - Company: {company} (Prakriti Enterprise)
            - Start Date: {start_date}
            - End Date: {end_date}
            - Salary: {salary}
            - Additional Context: {notes}

            STYLE GUIDELINES (Inspired by premium corporate communication):
            - Tone: Welcoming, professional, and inspiring. Use phrases like "delighted to extend", "begin your journey with us", "valuable asset to our team".
            - Structure: 
                1. Clear Subject Line.
                2. Professional Salutation.
                3. Enthusiastic opening paragraph mentioning the specific role and why they were chosen.
                4. Logistics section (Start date, location, responsibilities).
                5. Compensation & Benefits summary.
                6. Inspiring closing paragraph about the company's culture and impact.
                7. Formal sign-off.
            
            DON'T include the company header/logo, signature block, or closing salutation (like "Sincerely" or "With best wishes") in the markdown text, as they are handled by the UI. Just include the content from Subject onwards.
            Output in clean Markdown format with bold highlights for key terms.
            """
            
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"AI Generation Error: {e}")
            return generate_fallback(doc_type, name, position, company, start_date, end_date, salary, notes)
    else:
        return generate_fallback(doc_type, name, position, company, start_date, end_date, salary, notes)

def generate_fallback(doc_type, name, position, company, start_date, end_date, salary, notes):
    """Fallback logic with high-end manual templates."""
    # (Existing logic from previous version, kept as high-quality fallback)
    date_str = datetime.now().strftime("%B %d, %Y")
    
    if doc_type == "Offer Letter":
        content = f"""**Subject: Offer of Employment - {position}**

**Dear {name},**

We are absolutely delighted to extend to you an offer for the position of **{position}** at **Prakriti Enterprise**. Following our evaluation process, it is clear that your strong background and professional expertise will be a valuable asset to our organization.

You are scheduled to begin your journey with us on **{start_date}** at our Corporate Headquarters. This role includes a comprehensive compensation package of **{salary}** along with benefits aligned with our company standards.

At Prakriti Enterprise, we believe in shaping a sustainable future and we are excited about the energy and creativity you will bring to our projects. Please confirm your acceptance of this offer at your earliest convenience."""
    # ... (Other types follow same pattern)
    elif doc_type == "Internship Certificate":
        content = f"""**Subject: Official Certificate of Internship**

**Dear {name},**

This is to formally certify that **{name}** has successfully completed a professional internship at **Prakriti Enterprise** in the position of **{position}**. During the tenure from **{start_date}** to **{end_date}**, {name} has demonstrated exceptional dedication, technical aptitude, and a proactive approach towards learning and development.

Working closely with our core teams, {name} contributed significantly to various ongoing projects, showing a keen interest in nature-conscious solutions and corporate excellence. Their performance was consistently high, and they managed to tackle complex challenges with a positive attitude.

We appreciate the energy and fresh perspective brought to our organization during this period. We wish {name} the very best for all future academic and professional endeavors."""

    elif doc_type == "Experience Certificate":
        content = f"""**Subject: Professional Experience Certificate**

**To Whom It May Concern,**

This is to certify that **{name}** was employed with **Prakriti Enterprise** in the capacity of **{position}** from **{start_date}** to **{end_date}**.

During the tenure, {name} demonstrated exceptional technical proficiency and a collaborative work ethic. {name} played a vital role in achieving departmental goals and showed outstanding leadership and problem-solving skills. Their conduct was highly professional, and they consistently upheld the values of our organization.

We would like to thank {name} for their dedicated service and contributions to Prakriti Enterprise. We recommend them highly for any future professional roles and wish them great success in their career."""

    elif doc_type == "Appreciation Letter":
        content = f"""**Subject: Letter of Professional Appreciation**

**Dear {name},**

We are writing to express our sincere appreciation for your outstanding performance and dedication in your role as **{position}** at **Prakriti Enterprise**. Your recent contributions have significantly impacted our team's success and have set a benchmark for excellence.

Your commitment to the organization's goals and your ability to deliver high-quality results consistently is truly commendable. It is team members like you who drive the growth and success of Prakriti Enterprise.

Please accept this letter as a token of our gratitude for your hard work and commitment. We are proud to have you as part of our journey."""

    elif doc_type == "Relieving Letter":
        content = f"""**Subject: Official Relieving Letter**

**Dear {name},**

This is with reference to your resignation from the services of **Prakriti Enterprise**. We wish to inform you that you are officially relieved from your duties as **{position}** effective from the close of business hours on **{end_date}**.

We would like to place on record our appreciation for the services rendered by you during your tenure with the organization. All your dues have been settled as per the company policy.

We wish you all the very best in your future professional endeavors."""

    else:
        content = f"**Subject: Official {doc_type}**\n\n**Dear {name},**\n\nThis is a professional document regarding your role as **{position}** at **Prakriti Enterprise**. We appreciate your contributions during the period of **{start_date}** to **{end_date}**. Your performance has been evaluated and found to be in line with our corporate standards.\n\nNotes: {notes}"

    return content

# Backward compatibility for main.py
def generate_document(**kwargs):
    # Map kwargs to positional if needed or just use generate_document_ai
    return generate_document_ai(
        doc_type=kwargs.get('doc_type'),
        name=kwargs.get('name'),
        position=kwargs.get('position'),
        company=kwargs.get('company'),
        start_date=kwargs.get('start_date'),
        end_date=kwargs.get('end_date'),
        salary=kwargs.get('salary'),
        notes=kwargs.get('notes')
    )
