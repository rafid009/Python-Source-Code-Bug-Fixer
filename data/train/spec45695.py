import numpy as np 

def function(x):

	s2 = 2
	d9 = x
	paths = []
	try:
		if x >= 8:
			d9 = 9-d9
			paths.append(1)
		else:
			x = x-x
			s2 = s2/s2
			paths.append(2)
		if s2 <= 7:
			s2 = s2/d9
			x = 5-9
			paths.append(3)
		else:
			s2 = 2+s2
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		x = d9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))