import numpy as np 

def function(x):

	s7 = x
	a3 = 5
	paths = []
	try:
		if x < 9:
			s7 = a3/x
			a3 = 4/a3
			x = x-8
			paths.append(1)
		else:
			a3 = a3/a3
			paths.append(2)
		if a3 > 0:
			s7 = 2+s7
			a3 = 0-a3
			s7 = 1-a3
			paths.append(3)
		else:
			x = 3*0
			s7 = 9+s7
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		x = a3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))