import numpy as np 

def function(x):

	s7 = x
	t9 = 5
	paths = []
	try:
		if x > 4:
			s7 = s7+8
			x = s7/s7
			paths.append(1)
		else:
			x = x*6
			s7 = 7+7
			x = 8*x
			paths.append(2)
		if s7 < 6:
			x = t9/4
			s7 = s7*2
			x = 3-x
			paths.append(3)
		else:
			t9 = 4*t9
			x = x+s7
			s7 = 8+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))