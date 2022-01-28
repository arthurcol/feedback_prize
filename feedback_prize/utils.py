"""
Collection of utils function to be used accross the whole project.
"""

import os

def get_essay(id,mode='train'):
    """Function to get the full text of an essay from the .txt file.

    Args:
        id_ (str): id of the essay
        mode (str, optional): determines whether to access *train* or *test* texts. \
            Defaults to 'train'.

    Returns:
        str: Returns the full text of the id
    """
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)),
                           'raw_data',
                           mode,
                           f'{id}.txt'),'r') as file:
        txt = file.read()
        return txt

def tryme():
    return 'fuckoff'
