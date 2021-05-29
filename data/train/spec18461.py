import numpy as np 

def function(x):

	x6 = x
	s2 = x
	paths = []
	try:
		if x6 < 6:
			x6 = x6+s2
			x = x-6
			x6 = x/5
			paths.append(1)
		else:
			x = x*s2
			paths.append(2)
		if x > 5:
			s2 = x+s2
			paths.append(3)
		else:
			x = x6+4
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x = x6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))