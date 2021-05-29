import numpy as np 

def function(x):

	n4 = 7
	a2 = x
	x = 7
	paths = []
	try:
		if x >= 6:
			n4 = n4*x
			x = a2/4
			paths.append(1)
		else:
			a2 = n4-a2
			n4 = n4-0
			x = x/3
			paths.append(2)
		if n4 < 2:
			a2 = 6*a2
			x = a2*0
			n4 = 2+n4
			paths.append(3)
		else:
			a2 = 5-5
			n4 = 8+x
			a2 = 3/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))