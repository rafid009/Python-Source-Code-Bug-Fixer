import numpy as np 

def function(x):

	a3 = x
	v0 = x
	paths = []
	try:
		if x <= 5:
			a3 = a3/6
			v0 = 4-x
			paths.append(1)
		else:
			a3 = 5/5
			x = x-v0
			paths.append(2)
		if a3 <= 0:
			x = x-x
			v0 = v0/a3
			paths.append(3)
		else:
			a3 = a3/4
			v0 = x*a3
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		a3 = a3**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))