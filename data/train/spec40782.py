import numpy as np 

def function(x):

	o5 = 4
	s4 = 4
	paths = []
	try:
		if o5 > 0:
			s4 = s4/7
			x = 7+8
			paths.append(1)
		else:
			s4 = s4*o5
			paths.append(2)
		if x > 2:
			s4 = s4-5
			s4 = 8/s4
			paths.append(3)
		else:
			x = x/5
			s4 = x-x
			o5 = s4/x
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		x = s4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))