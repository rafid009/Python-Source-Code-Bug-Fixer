import numpy as np 

def function(x):

	t0 = 4
	s5 = x
	paths = []
	try:
		if s5 <= 1:
			t0 = s5+3
			paths.append(1)
		else:
			s5 = s5-6
			x = x*4
			paths.append(2)
		if x >= 9:
			x = 7/x
			s5 = s5*7
			paths.append(3)
		else:
			t0 = 3-x
			t0 = t0/s5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t0 = x**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))