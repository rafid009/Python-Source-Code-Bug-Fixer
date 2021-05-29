import numpy as np 

def function(x):

	s9 = x
	a7 = x
	x = 7
	paths = []
	try:
		if a7 >= 1:
			s9 = 5/a7
			x = x/1
			x = 4/4
			paths.append(1)
		else:
			x = 6-a7
			x = x*7
			paths.append(2)
		if a7 >= 9:
			a7 = a7/a7
			paths.append(3)
		else:
			a7 = 4*a7
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		x = a7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))