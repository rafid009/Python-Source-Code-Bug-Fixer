import numpy as np 

def function(x):

	a3 = 2
	n2 = 6
	paths = []
	try:
		if x >= 1:
			n2 = n2/5
			a3 = 7-4
			paths.append(1)
		else:
			a3 = 5*x
			a3 = n2*0
			paths.append(2)
		if a3 <= 2:
			a3 = 8+2
			x = x/6
			n2 = 7*x
			paths.append(3)
		else:
			a3 = 0/2
			x = x*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a3 = x**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))