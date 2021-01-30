import re

#regex to clip out answer section 
#pulls everything start from data section to static content
answer_section = re.compile(r"(?<=\"\{\\\"data\\\").*?(?=StaticContent)")

#regex to pull answer entry text
#right now it still grabs some other junk
answer_text = regex = re.compile(r"(?<=\[\{\\\\\\\"text\\\\\\\"\: \\\\\\\").*?(?=\\\\\\\")")

def extract_answers(html):
    try:
        all_answers = answer_section.findall(html)
        num_secs = len(all_answers)
        print(f"The number of sections extracted is {num_secs}")
        try:
            if num_secs == 1:
                answers = answer_text.findall(all_answers[0])
            return answers
        except:
            print("multiple sections were returned")
            pass
    except:
        print("fatal: regex failed or something else")
        
            