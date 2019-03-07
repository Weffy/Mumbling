def accum(user_input):
  accumulator = 1
  output_string = ""
  for letter in user_input:
    accum_string = letter*accumulator
    #print(output_string.capitalize())
    accumulator += 1
    output_string = output_string + "-" + accum_string.capitalize()
  return(output_string[1:len(output_string)])