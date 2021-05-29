import numpy as np 

def function(x):

	d4 = x
	s2 = 7
	paths = []
	try:
		if s2 < 9:
			x = x/2
			d4 = d4-s2
			d4 = d4-x
			paths.append(1)
		else:
			d4 = d4+d4
			x = 9-5
			paths.append(2)
		if x < 7:
			s2 = 5-s2
			x = d4/5
			paths.append(3)
		else:
			d4 = s2+d4
			x = x*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))