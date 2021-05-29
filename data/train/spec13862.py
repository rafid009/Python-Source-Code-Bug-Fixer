import numpy as np 

def function(x):

	j9 = x
	a7 = x
	x = 7
	paths = []
	try:
		if a7 <= 6:
			x = j9*5
			a7 = a7+5
			paths.append(1)
		else:
			a7 = a7+x
			x = 9/x
			paths.append(2)
		if a7 < 9:
			j9 = 5/5
			a7 = x-2
			j9 = j9+0
			paths.append(3)
		else:
			a7 = a7/2
			x = j9/2
			a7 = a7/a7
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		a7 = a7**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))