import numpy as np 

def function(x):

	s2 = 3
	t4 = 8
	paths = []
	try:
		if s2 < 8:
			x = x-x
			t4 = s2+t4
			s2 = s2*5
			paths.append(1)
		else:
			s2 = s2+x
			x = x/s2
			paths.append(2)
		if s2 < 4:
			x = x*6
			t4 = t4/8
			t4 = t4*x
			paths.append(3)
		else:
			x = x-5
			s2 = 2*s2
			x = 2+x
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