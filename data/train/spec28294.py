import numpy as np 

def function(x):

	t0 = 3
	s5 = x
	paths = []
	try:
		if t0 > 1:
			t0 = 5*t0
			paths.append(1)
		else:
			t0 = t0/5
			x = 9+8
			x = 2-x
			paths.append(2)
		if s5 <= 6:
			x = x-0
			paths.append(3)
		else:
			t0 = t0/6
			t0 = x-7
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		s5 = t0**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))