import numpy as np 

def function(x):

	n6 = x
	a1 = 6
	x = 4
	paths = []
	try:
		if a1 >= 6:
			x = x-8
			a1 = a1/n6
			paths.append(1)
		else:
			n6 = n6-a1
			x = 0+x
			x = a1/1
			paths.append(2)
		if x > 6:
			x = x/8
			a1 = x-6
			paths.append(3)
		else:
			n6 = n6+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))