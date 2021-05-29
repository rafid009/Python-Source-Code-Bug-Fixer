import numpy as np 

def function(x):

	a1 = x
	n2 = x
	paths = []
	try:
		if x <= 4:
			n2 = a1*3
			paths.append(1)
		else:
			a1 = a1-6
			paths.append(2)
		if a1 >= 2:
			a1 = n2-a1
			n2 = 9*n2
			x = x*5
			paths.append(3)
		else:
			a1 = 6*a1
			a1 = a1+n2
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		a1 = n2**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))