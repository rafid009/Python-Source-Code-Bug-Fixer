import numpy as np 

def function(x):

	e3 = 5
	n2 = x
	paths = []
	try:
		if x <= 2:
			n2 = 7*3
			n2 = 3*6
			e3 = 1-x
			paths.append(1)
		else:
			n2 = 9-2
			x = x/e3
			paths.append(2)
		if x <= 8:
			n2 = n2-2
			n2 = n2-e3
			paths.append(3)
		else:
			x = n2-0
			x = 0/e3
			e3 = n2+e3
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