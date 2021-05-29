import numpy as np 

def function(x):

	n1 = 4
	e1 = 5
	paths = []
	try:
		if n1 >= 9:
			e1 = x/8
			x = x*n1
			e1 = 6/e1
			paths.append(1)
		else:
			x = 7*x
			e1 = 3-e1
			e1 = 5/e1
			paths.append(2)
		if n1 <= 2:
			x = n1+n1
			paths.append(3)
		else:
			x = x/1
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		n1 = e1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))