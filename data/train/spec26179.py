import numpy as np 

def function(x):

	a0 = x
	t0 = 1
	x = 8
	paths = []
	try:
		if t0 < 9:
			a0 = t0*a0
			x = x/t0
			paths.append(1)
		else:
			x = x/7
			paths.append(2)
		if x < 7:
			x = x+0
			paths.append(3)
		else:
			x = x/x
			a0 = a0+a0
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