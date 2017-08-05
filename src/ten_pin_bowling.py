"""Uses bowling_score and the helper function translate score to read string of given bowling sheets and outputs the proper score."""


def translate_score(scorecard, i):
  """Assist with speedy translation of scorecard."""
  score_dict = {'X':10, 
  '9':9,
  '8':8,
  '7':7,
  '6':6,
  '5':5,
  '4':4,
  '3':3,
  '2':2,
  '1':1,
  '0':0
  }
  try:
    if scorecard[i] == 'X':
      return 10 + score_dict[scorecard[i+1]] + score_dict[scorecard[i+2]]
    elif scorecard[i] == '/':  
      return 10 - score_dict[scorecard[i - 1]] + score_dict[scorecard[i + 1]]
    else:
      return score_dict[scorecard[i]]
  except IndexError:
    if scorecard[i] == '/':
      return 10 - score_dict[scorecard[i - 1]]
    return 0
  except KeyError:
    return 10 + score_dict[scorecard[i+1]] + 10 - score_dict[scorecard[i+1]]



def bowling_score(frames):
  """Takes in a string and iterprets bowling score."""
  from functools import reduce
  scorecard = list(''.join(frames.split(' ')))
  if scorecard[-2] == 'X' or scorecard[-2] == '/':
    scorecard = [translate_score(scorecard, i) for i in range(len(scorecard))]
    return reduce(lambda x,y: x + y, scorecard) - scorecard[-1]
  scorecard = [translate_score(scorecard, i) for i in range(len(scorecard))]
  return reduce(lambda x,y: x + y, scorecard)
