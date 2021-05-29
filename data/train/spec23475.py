import numpy as np 

def function(x):

	a2 = x
	j6 = x
	paths = []
	try:
		if j6 >= 3:
			j6 = 3-7
			j6 = j6+6
			paths.append(1)
		else:
			a2 = 9-a2
			paths.append(2)
		if a2 >= 1:
			j6 = 2+x
			paths.append(3)
		else:
			x = j6/a2
			x = x-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))