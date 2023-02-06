from bayesian_node import BayesianNode

def replace_all(text, chars, replacement):
    for char in chars:
        text = text.replace(char, replacement)
    return text

def get_probability_dict(line):
    line = [replace_all(probability, [" ", "P", "(", ")", "\n"], "") for probability in line]
    line = "".join([char for char in line if (char != "")])
    line = line.split("=")
    line = [*line[0].split("|"), line[1]]
    return { "probability_of": line[0], "given": line[1], "equals": line[2] } if (len(line) == 3) else { "probability_of": line[0], "given": "", "equals": line[1] }

def get_parent_node(node, probabilities, probability_values, children):

    for probability in probabilities:

        if (probability["probability_of"] == node):
            probability_value = float(probability["equals"])
            probability_values[0][1] = round(probability_value, 3)
            probability_values[0][0] = round(1 - probability_value, 3)

        elif (probability["probability_of"] == f"!{node}"):
            probability_value = float(probability["equals"])
            probability_values[0][0] = round(probability_value, 3)
            probability_values[0][1] = round(1 - probability_value, 3)

    return BayesianNode(
        label=node,
        probability_values=probability_values,
        parents=[],
        children=children,
    )

def get_child_node(node, probabilities, probability_values, parents):
    for probability in probabilities:
        for index, parent in enumerate(parents):
            if (probability["probability_of"] == node and probability["given"] == parent):
                probability_value = float(probability["equals"])
                probability_values[index - 1][1] = round(probability_value, 3)
                probability_values[index - 1][0] = round(1 - probability_value, 3)
            elif (probability["probability_of"] == f"!{node}" and probability["given"] == parent):
                probability_value = float(probability["equals"])
                probability_values[index - 1][0] = round(probability_value, 3)
                probability_values[index - 1][1] = round(1 - probability_value, 3)
            elif (probability["probability_of"] == node and probability["given"] == f"!{parent}"):
                probability_value = float(probability["equals"])
                probability_values[index][1] = round(probability_value, 3)
                probability_values[index][0] = round(1 - probability_value, 3)
            elif (probability["probability_of"] == f"!{node}" and probability["given"] == f"!{parent}"):
                probability_value = float(probability["equals"])
                probability_values[index][0] = round(probability_value, 3)
                probability_values[index][1] = round(1 - probability_value, 3)
    return BayesianNode(
        label=node,
        probability_values=probability_values,
        parents=parents,
        children=[],
    )
