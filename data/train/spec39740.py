import numpy as np 

def function(x):

	v6 = x
	s4 = x
	x = 8
	paths = []
	try:
		if v6 > 2:
			v6 = v6*4
			paths.append(1)
		else:
			v6 = v6+v6
			s4 = s4*3
			s4 = s4-3
			paths.append(2)
		if s4 > 6:
			v6 = v6*8
			paths.append(3)
		else:
			v6 = 1-v6
			x = x-v6
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		s4 = v6**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))