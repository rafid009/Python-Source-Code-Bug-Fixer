import numpy as np 

def function(x):

	t5 = 2
	s8 = x
	paths = []
	try:
		if x > 7:
			x = 6/1
			paths.append(1)
		else:
			x = x*3
			t5 = 8-t5
			s8 = s8*3
			paths.append(2)
		if t5 <= 2:
			x = 0-x
			paths.append(3)
		else:
			x = s8-x
			t5 = 9+2
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