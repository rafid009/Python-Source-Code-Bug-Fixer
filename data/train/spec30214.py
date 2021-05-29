import numpy as np 

def function(x):

	a7 = 7
	v7 = x
	paths = []
	try:
		if v7 <= 0:
			a7 = a7/4
			paths.append(1)
		else:
			v7 = v7+a7
			v7 = v7/8
			paths.append(2)
		if a7 < 0:
			v7 = x/v7
			paths.append(3)
		else:
			v7 = x-v7
			a7 = 3+x
			a7 = x-a7
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		a7 = v7**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))