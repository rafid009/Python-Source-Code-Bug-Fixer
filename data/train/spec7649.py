import numpy as np 

def function(x):

	s8 = 4
	t1 = x
	paths = []
	try:
		if t1 >= 2:
			s8 = s8/8
			t1 = 8-5
			paths.append(1)
		else:
			t1 = 7/t1
			paths.append(2)
		if t1 < 1:
			t1 = t1-x
			s8 = t1*s8
			paths.append(3)
		else:
			x = x+s8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s8 = x**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))