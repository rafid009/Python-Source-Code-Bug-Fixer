import numpy as np 

def function(x):

	o2 = 1
	s2 = 4
	paths = []
	try:
		if o2 > 6:
			o2 = o2+2
			x = x*s2
			o2 = o2/8
			paths.append(1)
		else:
			s2 = x+x
			paths.append(2)
		if s2 > 2:
			x = x*9
			paths.append(3)
		else:
			x = 2-8
			s2 = 1/3
			x = x-7
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