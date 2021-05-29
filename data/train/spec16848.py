import numpy as np 

def function(x):

	s2 = 1
	t3 = 7
	paths = []
	try:
		if t3 <= 9:
			s2 = 9*s2
			paths.append(1)
		else:
			x = x-3
			paths.append(2)
		if t3 < 0:
			x = 3*x
			paths.append(3)
		else:
			x = x*8
			x = 1/x
			s2 = s2+s2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t3 = x**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))