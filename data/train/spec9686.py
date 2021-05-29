import numpy as np 

def function(x):

	s5 = x
	t8 = 1
	paths = []
	try:
		if s5 > 7:
			t8 = 4*2
			x = x*6
			paths.append(1)
		else:
			t8 = x-t8
			paths.append(2)
		if x > 3:
			t8 = 9*t8
			paths.append(3)
		else:
			x = t8/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s5 = x**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))