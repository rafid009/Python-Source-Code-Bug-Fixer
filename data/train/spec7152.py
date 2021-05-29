import numpy as np 

def function(x):

	d7 = x
	s2 = x
	paths = []
	try:
		if x >= 1:
			x = s2-x
			paths.append(1)
		else:
			s2 = 6*s2
			x = x*d7
			d7 = 5+d7
			paths.append(2)
		if d7 > 6:
			s2 = s2-2
			s2 = d7*2
			paths.append(3)
		else:
			s2 = s2/3
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		x = s2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))