def arithmetic_arranger(problems, show_answer=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []
    answers = []
    for problem in problems:
        operator = ""
        operand1 = ""
        operand2 = ""
        for char in problem:
            if char.isdigit():
                if operator == "":
                    operand1 += char
                else:
                    operand2 += char
            elif char in ["+", "-"]:
                operator = char
            else:
                return "Error: Operator must be '+' or '-'."
        
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        operand1 = operand1.rjust(4)
        operand2 = operand2.rjust(4)
        operator = operator.rjust(2)
        if operator == "+":
            answer = str(int(operand1) + int(operand2)).rjust(4)
            answers.append(answer)
        else:
            answer = str(int(operand1) - int(operand2)).rjust(4)
            answers.append(answer)
        arranged_problems.append(f"{operand1}    {operator} {operand2}\n-----")

    arranged_problems = "    ".join(arranged_problems)

    if show_answer:
        answers = "    ".join(answers)
        return f"{arranged_problems}\n{answers}"
    else:
        return arranged_problems
