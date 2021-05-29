import numpy as np 

def function(x):

	s5 = 6
	o6 = x
	paths = []
	try:
		if x > 7:
			s5 = 6-o6
			s5 = 1*s5
			o6 = o6-x
			paths.append(1)
		else:
			o6 = 7*s5
			x = s5/9
			paths.append(2)
		if x < 5:
			x = x/x
			x = x-o6
			o6 = s5-9
			paths.append(3)
		else:
			o6 = 1*6
			x = x*6
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		s5 = o6**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))