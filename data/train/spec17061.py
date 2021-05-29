import numpy as np 

def function(x):

	t4 = x
	s0 = x
	paths = []
	try:
		if t4 > 0:
			t4 = 1+s0
			x = t4-5
			t4 = t4+1
			paths.append(1)
		else:
			s0 = 4/6
			paths.append(2)
		if x > 0:
			s0 = t4/s0
			s0 = s0+x
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		s0 = t4**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))