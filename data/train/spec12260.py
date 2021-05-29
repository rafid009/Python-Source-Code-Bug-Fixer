import numpy as np 

def function(x):

	n2 = 2
	e1 = 2
	paths = []
	try:
		if x <= 3:
			x = x-6
			e1 = e1-0
			e1 = 8/e1
			paths.append(1)
		else:
			e1 = e1-x
			e1 = e1/5
			n2 = n2/9
			paths.append(2)
		if e1 > 8:
			n2 = n2/9
			x = 0+x
			paths.append(3)
		else:
			x = x/e1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n2 = x**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))