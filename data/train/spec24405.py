import numpy as np 

def function(x):

	a2 = 7
	w6 = x
	paths = []
	try:
		if a2 > 9:
			w6 = 9-w6
			a2 = 1-a2
			paths.append(1)
		else:
			a2 = 5+w6
			paths.append(2)
		if a2 > 9:
			a2 = 8*x
			paths.append(3)
		else:
			a2 = a2/6
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		a2 = w6**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))