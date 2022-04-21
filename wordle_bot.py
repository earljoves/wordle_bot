def convert_to_emoji(result):
  output = ''
  for r in result:
    if r == 0:
      output += '⬛'
    elif r == 1:
      output += '🟨'
    elif r == 2:
      output += '🟩'
  return output

def get_result(test_word, key_word):
  test_word = test_word.lower()
  key_word = key_word.lower()
  output = [0, 0, 0, 0, 0]

  for i in range(len(test_word)):
    # find green squares
    if test_word[i] == key_word[i]:
      output[i] = 2
    # find yellow squares
    elif key_word.find(test_word[i]) != -1:
      # not a duplicate
      if test_word[:i].find(test_word[i]) == -1:
        output[i] = 1
      # is a duplicate
      else:
        # create temp string replacing the duplicated letter in the key word
        key_word_replaced = key_word.replace(test_word[i], '', 1)

        # duplicate input letter also duplicated in key word
        if key_word_replaced.find(test_word[i]) != -1:
          output[i] = 1
        # duplicate input letter NOT duplicated in key word
        else:
          output[i] = 0
    else:
      output[i] = 0

  return output

def main():
  pass

if __name__ == '__main__':
  main()
