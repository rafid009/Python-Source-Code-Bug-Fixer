import numpy as np 

def function(x):

	v1 = 5
	a3 = 2
	paths = []
	try:
		if a3 <= 8:
			a3 = a3/7
			paths.append(1)
		else:
			a3 = 4/a3
			paths.append(2)
		if v1 > 6:
			v1 = 2/3
			x = 2+v1
			a3 = a3-x
			paths.append(3)
		else:
			a3 = x-a3
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