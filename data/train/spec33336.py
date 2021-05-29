import numpy as np 

def function(x):

	s5 = 9
	o0 = x
	paths = []
	try:
		if x <= 8:
			o0 = 9*o0
			paths.append(1)
		else:
			s5 = 7-s5
			s5 = s5/5
			o0 = 0-o0
			paths.append(2)
		if o0 >= 5:
			s5 = s5-9
			paths.append(3)
		else:
			o0 = o0+1
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		s5 = s5**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))