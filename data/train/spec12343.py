import numpy as np 

def function(x):

	s7 = 5
	o1 = 9
	paths = []
	try:
		if s7 <= 7:
			s7 = x*s7
			o1 = 4+o1
			paths.append(1)
		else:
			s7 = o1-5
			x = x*3
			paths.append(2)
		if s7 < 5:
			s7 = 4*o1
			s7 = 2-5
			paths.append(3)
		else:
			s7 = s7/o1
			o1 = o1-s7
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		x = o1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))