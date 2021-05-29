import numpy as np 

def function(x):

	a0 = 1
	a1 = 3
	paths = []
	try:
		if x <= 3:
			a0 = 0+a0
			a1 = a1-a1
			paths.append(1)
		else:
			a0 = a0+8
			a1 = x-a1
			paths.append(2)
		if a0 < 2:
			a1 = 1*a1
			x = x/2
			x = x*5
			paths.append(3)
		else:
			a0 = 5-a0
			a0 = a0*3
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		a1 = a0**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))