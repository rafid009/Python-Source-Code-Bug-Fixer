import numpy as np 

def function(x):

	s0 = x
	t0 = 1
	paths = []
	try:
		if s0 > 5:
			x = t0*1
			paths.append(1)
		else:
			x = x-9
			t0 = t0*3
			paths.append(2)
		if x >= 0:
			s0 = s0-0
			paths.append(3)
		else:
			x = x-t0
			t0 = t0/x
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		t0 = t0**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))