import numpy as np 

def function(x):

	s4 = x
	o5 = 7
	paths = []
	try:
		if x <= 2:
			o5 = o5-3
			x = x*x
			paths.append(1)
		else:
			s4 = s4+7
			paths.append(2)
		if o5 > 5:
			s4 = o5+s4
			x = x-x
			paths.append(3)
		else:
			o5 = o5/8
			o5 = o5-s4
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		s4 = o5**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))