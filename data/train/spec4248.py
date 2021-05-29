import numpy as np 

def function(x):

	v4 = x
	s4 = 6
	x = 0
	paths = []
	try:
		if x < 6:
			s4 = 2-s4
			s4 = 0-0
			s4 = s4*8
			paths.append(1)
		else:
			v4 = v4+s4
			s4 = v4-x
			paths.append(2)
		if x < 1:
			v4 = v4+7
			paths.append(3)
		else:
			x = 6*x
			s4 = s4/1
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		x = v4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))