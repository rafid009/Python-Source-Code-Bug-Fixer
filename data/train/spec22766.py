import numpy as np 

def function(x):

	s8 = 8
	a0 = 3
	x = 9
	paths = []
	try:
		if x <= 4:
			s8 = s8/3
			paths.append(1)
		else:
			a0 = 8*a0
			a0 = 7*a0
			a0 = 5-7
			paths.append(2)
		if x < 6:
			s8 = s8/8
			s8 = 2-s8
			paths.append(3)
		else:
			x = x-7
			x = x*6
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		a0 = a0**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))