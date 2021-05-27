import numpy as np 

def function(x):

	s5 = 1
	t7 = x
	x = 4
	paths = []
	try:
		if s5 <= 7:
			x = 1-x
			paths.append(1)
		else:
			x = x*5
			paths.append(2)
		if t7 < 5:
			x = 8-1
			paths.append(3)
		else:
			x = x-s5
			s5 = 3+s5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t7 = x**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))