def split_map(unsplit_list_element):
    split_list_element = unsplit_list_element.split(' ')
    return split_list_element

def arithmetic_arranger(problems, show_answers=False):
    split_problems = list(map(split_map, problems))
    list_line1 = []
    list_line2 = []
    list_dashes = []
    list_result = []

    for problem in split_problems:
        if len(problems) > 5:
            return 'Error: Too many problems.'
            
        if problem[1] != '+' and problem[1] != '-':
            return 'Error: Operator must be \'+\' or \'-\'.'
        
        if not problem[0].isdigit() or not problem[2].isdigit():
            return 'Error: Numbers must only contain digits.'
            
        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # length of the number + 2 for the operator
        min_first_line_width = 2 + len(problem[0])
        min_second_line_width = 2 + len(problem[2])
        line_width = max(min_first_line_width, min_second_line_width)

        
        
        if problem[1] == '+':
            solution = int(problem[0]) + int(problem[2])
        else:
            solution = int(problem[0]) - int(problem[2])
        
        solution_text = str(solution)

        list_line1.append(' ' * (line_width - len(problem[0])) + problem[0])
        list_line2.append(problem[1] + ' ' * (line_width - len(problem[2]) - 1)  + problem[2])
        list_dashes.append('-' * line_width)
        list_result.append(' ' * (line_width - len(solution_text)) + solution_text)
    
    string_line1 = '    '.join(list_line1)
    string_line2 = '    '.join(list_line2)
    string_dashes = '    '.join(list_dashes)
    string_result = '    '.join(list_result)
    
    if show_answers:
        return string_line1 + '\n' + string_line2 + '\n' + string_dashes + '\n' + string_result
    else:
        return string_line1 + '\n' + string_line2 + '\n' + string_dashes
