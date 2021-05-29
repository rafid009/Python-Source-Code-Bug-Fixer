import numpy as np 

def function(x):

	t1 = 5
	s0 = x
	x = x
	paths = []
	try:
		if x >= 3:
			t1 = x-0
			s0 = 0/s0
			paths.append(1)
		else:
			t1 = 7-8
			s0 = 3*8
			paths.append(2)
		if t1 <= 3:
			s0 = 5+s0
			x = 7-x
			paths.append(3)
		else:
			x = x+8
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		s0 = t1**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))