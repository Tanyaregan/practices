data = "blah blah %tanyaregan@gmail.com 33 44 567"

at_sign_pos = data.find('@')
print at_sign_pos

end_pos = data.find(' ', at_sign_pos)
print end_pos

domain = data[at_sign_pos+1:end_pos]
print domain
