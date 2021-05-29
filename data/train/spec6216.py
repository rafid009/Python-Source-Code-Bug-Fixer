import numpy as np 

def function(x):

	v5 = 3
	s4 = x
	paths = []
	try:
		if x > 2:
			s4 = 9/6
			paths.append(1)
		else:
			v5 = 7/v5
			x = v5+x
			paths.append(2)
		if x < 4:
			s4 = s4*4
			paths.append(3)
		else:
			x = 3/x
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		v5 = s4**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))