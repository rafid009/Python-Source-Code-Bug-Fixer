import numpy as np 

def function(x):

	s2 = x
	f3 = 2
	paths = []
	try:
		if x <= 2:
			f3 = s2+5
			f3 = f3+7
			paths.append(1)
		else:
			s2 = 0-s2
			f3 = 1/f3
			paths.append(2)
		if x > 2:
			x = 8+f3
			paths.append(3)
		else:
			s2 = x-3
			s2 = 1*f3
			f3 = x-9
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		x = s2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))