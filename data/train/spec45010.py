import numpy as np 

def function(x):

	a4 = 6
	v7 = x
	paths = []
	try:
		if v7 > 4:
			x = 4+v7
			paths.append(1)
		else:
			a4 = 5*a4
			paths.append(2)
		if a4 > 7:
			a4 = 6+5
			a4 = 8*a4
			paths.append(3)
		else:
			a4 = 5-5
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		v7 = v7**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))