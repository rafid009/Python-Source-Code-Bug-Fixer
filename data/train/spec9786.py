import numpy as np 

def function(x):

	t0 = 6
	s9 = x
	paths = []
	try:
		if t0 < 0:
			x = x/2
			t0 = 1*t0
			x = 0*x
			paths.append(1)
		else:
			x = x*8
			paths.append(2)
		if t0 > 5:
			s9 = s9-3
			paths.append(3)
		else:
			x = 7-1
			x = 8+0
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		s9 = s9**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))