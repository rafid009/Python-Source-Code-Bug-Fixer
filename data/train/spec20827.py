import numpy as np 

def function(x):

	a0 = 2
	a4 = x
	paths = []
	try:
		if x < 9:
			x = 8-a4
			paths.append(1)
		else:
			x = a4-3
			a0 = 4+a0
			paths.append(2)
		if a4 > 7:
			x = x*1
			a4 = a0/8
			paths.append(3)
		else:
			a4 = a4*x
			a0 = a0*a4
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		a4 = a0**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))