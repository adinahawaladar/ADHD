adhd_questions = [
    {"question": "Do you often have trouble concentrating on tasks?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you struggle to complete long tasks?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you frequently forget appointments or deadlines?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you often feel restless or fidgety?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you find it difficult to stay organized?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you get easily distracted by external stimuli?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you frequently lose important items like keys or wallets?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you have difficulty following through on instructions?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you tend to procrastinate on important tasks?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you feel overwhelmed by daily responsibilities?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you struggle with time management?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you often interrupt others while they are speaking?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you have trouble sitting still for extended periods?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you find it hard to focus on conversations?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you struggle to complete work or school assignments on time?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you frequently feel impulsive and act without thinking?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you get easily frustrated or impatient?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you struggle to prioritize tasks?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you find it difficult to unwind or relax?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you often feel mentally exhausted from trying to focus?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you have difficulty remembering details of conversations?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you often feel restless and struggle to stay seated?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you struggle to maintain eye contact during conversations?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you find it hard to complete household chores without distraction?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you frequently misplace everyday items?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you struggle to listen attentively in meetings or classes?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you get easily sidetracked from a task by unrelated thoughts?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you frequently feel disorganized and overwhelmed?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you find it hard to follow multi-step instructions?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you frequently blurt out answers before a question is completed?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you feel restless even in quiet environments?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you avoid tasks that require sustained mental effort?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you struggle with impulse control in social situations?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you find it hard to stick to long-term projects?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you frequently feel distracted even when doing enjoyable activities?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you struggle to transition from one task to another?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you find it difficult to remain seated during meals?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you tend to talk excessively in conversations?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you feel anxious when required to stay still for long periods?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you frequently miss important details in written instructions?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you often feel like your thoughts are scattered?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you have difficulty following a daily routine?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you often make careless mistakes in work or school?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you feel overwhelmed when starting new tasks?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you frequently find yourself daydreaming?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you struggle to remember names and faces?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you often feel mentally exhausted from trying to concentrate?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you struggle with self-motivation to complete projects?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you often need multiple reminders to complete simple tasks?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you find it hard to manage multiple responsibilities at once?", "options": ["Never", "Sometimes", "Often", "Always"]},
    {"question": "Do you feel easily frustrated when working on repetitive tasks?", "options": ["Never", "Sometimes", "Often", "Always"]},
]

for i in range(4, 201):
    adhd_questions.append(
        {
            "question": f"Sample ADHD question {i}?",
            "options": ["Never", "Sometimes", "Often", "Always"]
        }
    )

def get_questions():
    return adhd_questions