import numpy as np 

def function(x):

	v7 = 7
	a1 = x
	paths = []
	try:
		if x < 0:
			v7 = 9+v7
			a1 = a1-v7
			paths.append(1)
		else:
			v7 = 9-2
			a1 = 6-a1
			paths.append(2)
		if v7 > 7:
			v7 = a1/2
			paths.append(3)
		else:
			v7 = 9/v7
			a1 = 3*x
			a1 = 9/a1
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		a1 = v7**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))