import numpy as np 

def function(x):

	e1 = 3
	n6 = 5
	paths = []
	try:
		if x >= 3:
			n6 = 6-6
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if n6 < 8:
			e1 = x/3
			paths.append(3)
		else:
			e1 = e1*7
			x = 9/x
			n6 = n6+1
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		n6 = e1**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))