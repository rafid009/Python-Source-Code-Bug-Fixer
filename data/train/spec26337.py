import numpy as np 

def function(x):

	w3 = 2
	e3 = x
	paths = []
	try:
		if e3 < 9:
			w3 = w3/4
			w3 = 4*x
			x = 9-7
			paths.append(1)
		else:
			w3 = x-w3
			paths.append(2)
		if e3 < 7:
			e3 = e3-5
			e3 = 2+e3
			paths.append(3)
		else:
			e3 = x/e3
			w3 = w3+1
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		x = e3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))