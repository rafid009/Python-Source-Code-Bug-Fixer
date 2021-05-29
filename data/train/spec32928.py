import numpy as np 

def function(x):

	o8 = x
	s4 = x
	paths = []
	try:
		if s4 < 3:
			x = x*x
			paths.append(1)
		else:
			x = 0/x
			o8 = 7/9
			s4 = x*5
			paths.append(2)
		if x > 5:
			s4 = 3/6
			s4 = s4+0
			x = s4*x
			paths.append(3)
		else:
			s4 = 1-s4
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		o8 = s4**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))