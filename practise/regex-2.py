import re

text_to_match = """{Research Proposal: How Can Study Be Improved with New Techniques and AI Technologies?

Title/Topic:

How Can Study Be Improved? The Role of New Techniques and AI Technologies in Education

Problem/Issue:

Many students experience difficulties due to old teaching methods such as memorizing facts and simply reading without much involvement. New approaches and technologies, including artificial intelligence (AI), can improve learning efficiency, help students remember information better, and make learning more enjoyable. This research looks at the best tools and strategies to help students learn more effectively.

Aim and Objectives:

The aim of this research is to investigate how modern study techniques and AI tools can improve learning outcomes for students.

Objectives:
• Compare traditional study methods with modern techniques like active recall and spaced repetition.
• Evaluate the impact of AI tools (e.g., ChatGPT, DeepSeek) on students’ academic performance.
• Identify which study methods students find most effective.

Method of Research:
•	Type of Research: Survey .
•	Sample Population: First-year university students (ages 17-18).
•	Location: KBTU University.
•	Data Collection Techniques:
•	Questionnaires – online questionnaire to assess students’ preferred study methods'''}"""




pattern = re.sub("a","&",text_to_match)