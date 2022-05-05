name = "Tim"
message = f"Hello, {name} would you like to learn some Python Today?"
print(message)

low = name.lower()
print(low)
case = name.upper()
print(case)
proper = name.title()
print(proper)

quote_auther = "albert einstein"
right_name = quote_auther.title()

quote = "\"A person who never made a mistake never tried anything new.\""

put_together = f"{right_name} {quote}"
print(put_together)

person = "  john Doe "
partly_fixed = person.lstrip()
other_part = person.rstrip()
real_name = partly_fixed,other_part
print(real_name)
fixed_name = person.strip()
print(fixed_name)
message = f"{fixed_name} --There was a little boy, who needed all the help he could get.\n\t\t But no one realized that as hard as he tried,\n\t\t it was hard for him to be normal. \n\t\t But no one ever seemed to care enough. \n\t\tno matter how hard he tried to show everyone."
print(message)
