import numpy as np 

def function(x):

	t3 = x
	s7 = x
	paths = []
	try:
		if t3 <= 6:
			x = 1-0
			x = 2*x
			paths.append(1)
		else:
			x = 9/t3
			t3 = 3*t3
			t3 = 6*s7
			paths.append(2)
		if x > 2:
			x = 4+5
			x = 8-7
			paths.append(3)
		else:
			t3 = 2*t3
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		s7 = s7**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))