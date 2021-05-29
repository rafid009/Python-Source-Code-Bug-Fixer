import numpy as np 

def function(x):

	n1 = 5
	a9 = 1
	paths = []
	try:
		if n1 <= 4:
			a9 = 6+a9
			x = 7*0
			x = x*a9
			paths.append(1)
		else:
			a9 = a9+a9
			n1 = n1+x
			x = 9/7
			paths.append(2)
		if n1 <= 8:
			a9 = a9/4
			x = 6-x
			x = x*3
			paths.append(3)
		else:
			x = x-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))