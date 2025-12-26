import gradio as gr

def campus_bot(question):
    question = question.lower()

    if "exam" in question:
        return "📅 Exams start from 10th March.\nMore info: https://iips.edu.in/"

    elif "syllabus" in question:
        return "📚 Syllabus is available under Academics.\nhttps://iips.edu.in/syllabus.php"

    elif "faculty" in question:
        return "👩‍🏫 Faculty details:\nhttps://iips.edu.in/faculty_profile.php"

    elif "office" in question:
        return "🏢 Office hours: 10 AM — 4 PM (Mon–Fri)\nhttps://iips.edu.in/"

    elif "academic calendar" in question or "calendar" in question:
        return "🗓️ Academic Calendar (July–Dec 2025):\nhttps://iips.edu.in/static/pdf/acc_calendar/AcademicCalenderJulyDec2025.pdf"

    elif "fee" in question or "fees" in question or "fee structure" in question:
        return "💰 Fee Structure details:\nhttps://iips.edu.in/fee_structure.php"

    elif "scholarship" in question:
        return "🎓 Scholarship details:\nhttps://iips.edu.in/scholarship.php"

    elif "placement" in question:
        return "💼 Placement statistics & Training Cell:\nhttps://iips.edu.in/placement.php"

    elif "result" in question:
        return "📊 Results announced here:\nhttps://iips.edu.in/results.php"

    elif "time table" in question or "timetable" in question:
        return "📘 Time Table will be updated soon on the college website.\nhttps://iips.edu.in/"

    elif "admission" in question:
        return "📝 Admission guidelines and eligibility:\nhttps://iips.edu.in/admission.php"

    elif "contact" in question:
        return "☎ Contact details:\nhttps://iips.edu.in/contact_us.php"

    else:
        return "🤖 Sorry! I’m still learning.\nYou can ask: exams, syllabus, fees, placement, scholarships, results, timetable"

# Interface
demo = gr.Interface(
    fn=campus_bot,
    inputs="text",
    outputs="text",
    title="🎓 AI Campus Helpdesk",
    description="Quick answers about IIPS Indore — Exams, Fees, Placements, Scholarships & more!",
    examples=[]  
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)



   
