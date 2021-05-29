import numpy as np 

def function(x):

	t3 = x
	s4 = x
	paths = []
	try:
		if t3 <= 0:
			x = 6+x
			paths.append(1)
		else:
			t3 = 6/2
			x = s4*x
			paths.append(2)
		if x >= 1:
			t3 = 9-9
			x = s4-1
			t3 = s4+4
			paths.append(3)
		else:
			x = x+7
			t3 = x+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s4 = x**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))