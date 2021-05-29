import numpy as np 

def function(x):

	n1 = 8
	e3 = 1
	paths = []
	try:
		if e3 < 9:
			e3 = e3-3
			n1 = n1*n1
			n1 = e3-8
			paths.append(1)
		else:
			e3 = 9*e3
			paths.append(2)
		if x <= 8:
			e3 = e3/4
			paths.append(3)
		else:
			x = x*0
			x = 9*9
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		n1 = e3**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))