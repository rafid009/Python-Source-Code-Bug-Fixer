import numpy as np 

def function(x):

	s6 = x
	o5 = 5
	paths = []
	try:
		if s6 >= 9:
			x = 1*x
			s6 = 1*s6
			o5 = s6-o5
			paths.append(1)
		else:
			o5 = o5+o5
			o5 = 3-6
			x = x-3
			paths.append(2)
		if x > 3:
			o5 = o5+o5
			s6 = s6/x
			paths.append(3)
		else:
			o5 = o5/1
			x = x*4
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		o5 = s6**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))