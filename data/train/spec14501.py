import numpy as np 

def function(x):

	a5 = x
	s9 = x
	paths = []
	try:
		if a5 >= 6:
			a5 = a5+9
			a5 = 2-a5
			a5 = a5+6
			paths.append(1)
		else:
			x = 2-x
			x = x+0
			s9 = 3/s9
			paths.append(2)
		if x < 3:
			a5 = a5/6
			paths.append(3)
		else:
			s9 = 3/5
			a5 = 2*a5
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))