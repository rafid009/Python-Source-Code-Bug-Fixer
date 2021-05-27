import numpy as np 

def function(x):

	t0 = 4
	j7 = 7
	paths = []
	try:
		if x <= 2:
			j7 = j7+t0
			paths.append(1)
		else:
			x = x+6
			x = 7-x
			x = x+x
			paths.append(2)
		if x <= 0:
			x = x-7
			j7 = 9+j7
			t0 = t0/9
			paths.append(3)
		else:
			x = 5*x
			t0 = 3/t0
			x = x+x
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