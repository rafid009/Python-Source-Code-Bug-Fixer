import numpy as np 

def function(x):

	n3 = 0
	a6 = 9
	paths = []
	try:
		if n3 >= 2:
			n3 = x-4
			paths.append(1)
		else:
			n3 = 9-n3
			x = x*2
			paths.append(2)
		if n3 <= 3:
			a6 = 6-x
			a6 = a6+1
			a6 = a6+x
			paths.append(3)
		else:
			n3 = n3-8
			x = x-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a6 = x**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))