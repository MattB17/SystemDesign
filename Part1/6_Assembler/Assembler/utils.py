"""A set of utility functions used by the assembler.

"""
import re


def remove_comment_from_instruction(instruction_str):
    """Removes any inline comments from `instruction_str`.

    Parameters
    ----------
    instruction_str: str
        A string representing the instruction to be processed.

    Returns
    -------
    str
        The string obtained from `instruction_str` after removing any
        inline comments.

    """
    comment_pos = instruction_str.find("//")
    if comment_pos == -1:
        return instruction_str.strip()
    return instruction_str[:comment_pos].strip()


def get_instruction_components(instruction_str):
    """Retrieves the components of `instruction_str`.

    Parameters
    ----------
    instruction_str: str
        A string representing the instruction to be processed.

    Returns
    -------
    list
        A list of strings containing the components of the instruction.

    """
    instruction_str = remove_comment_from_instruction(instruction_str)
    if instruction_str[0] == "@":
        return [instruction_str[1:]]
    return [command.strip().replace(" ", "")
            for command in re.split('[=;]', instruction_str)]
