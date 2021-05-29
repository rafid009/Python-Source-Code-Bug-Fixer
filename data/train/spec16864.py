import numpy as np 

def function(x):

	w5 = x
	a4 = x
	paths = []
	try:
		if x > 4:
			w5 = w5+a4
			a4 = 5-x
			a4 = x*4
			paths.append(1)
		else:
			w5 = 7*9
			w5 = w5/1
			paths.append(2)
		if x >= 5:
			x = x*4
			a4 = 3+a4
			paths.append(3)
		else:
			a4 = 9-a4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a4 = x**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))