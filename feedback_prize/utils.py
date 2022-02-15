"""
Collection of utils function to be used accross the whole project.
"""

import os
from IPython.display import HTML

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

def slicering(ps,txt):
    """
    Allow for predictionstring to match with corresponding words of an essay.
    Given a predictionstring of a portion of a text and the full text, the
    function returns the portion of the text corresponding to the predictionstring.

    Args:
        ps (str): predictionstring of a discourse
        txt (str): full text of an essay

    Returns:
        str: portion of the text corresponding to the predictionstring
    """
    ps_l = ps.split()
    txt = txt.split()

    return ' '.join(txt[int(ps_l[0]):int(ps_l[-1])+1])


def css():
    """
    Apply custom.css into the notebook

    Returns:
        str: HTML style tag
    """
    styles = open("./styles/custom.css", "r").read()
    return HTML('<style>'+styles+'</style>')


def render_html(df):
    """
    Transforms each discourse into a html string with appropriates tags for
    visualization.

    Args:
        df (DataFrame): dataframe containing discourse_type and discourse_text

    Returns:
        str: html string
    """
    if 'class' in df.keys():
        class_='class'
    else:
        class_='discourse_type'

    html = "<{0} style='padding: 2px'>{1} <strong> [{0}] </strong></{0}>"\
            .format(df[class_],df['discourse_text'])

    return html

def comparison_text(prediction, ground_truth):
    """
    Allow for visual comparison of an essay with predicted classes vs the essay
    with the true classes

    Args:
        prediction (str): essay with predicted classes in html formatting
        ground_truth (str): essay with true classes in html formatting

    Returns:
        html: visual table
    """


    html = f"""
    <div class="content">
     <span style="font-size:16px">Legend --></span>
      <lead>Lead</lead>
      <Position>Position</Position>
      <Claim>Claim</Claim>
      <Counterclaim>Counterclaim</Counterclaim>
      <Rebuttal>Rebuttal</Rebuttal>
      <Evidence>Evidence</Evidence>
      <Concluding_Statement>Concluding_Statement</Concluding_Statement>
    </div>

    <div class="row">
      <div class="column">
        <h2 class="title">Prediction</h2>
        <p style="text-align:justify">{prediction}</p>
      </div>
      <div class="column">
        <h2 class="title">Ground Truth</h2>
        <p style="text-align:justify">{ground_truth}</p>
      </div>
    </div>
    """
    return HTML(html)

if __name__ == "__main__":
    pass
