import numpy as np 

def function(x):

	a6 = x
	i7 = 9
	paths = []
	try:
		if a6 <= 7:
			a6 = 4+a6
			a6 = a6-7
			paths.append(1)
		else:
			i7 = a6/x
			paths.append(2)
		if a6 < 9:
			x = x/a6
			x = a6*x
			paths.append(3)
		else:
			x = a6-x
			i7 = a6*i7
			i7 = 6-a6
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		i7 = i7**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))