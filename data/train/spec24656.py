import numpy as np 

def function(x):

	a7 = 5
	d2 = x
	paths = []
	try:
		if d2 <= 9:
			x = 9/x
			paths.append(1)
		else:
			a7 = a7*d2
			d2 = a7-d2
			paths.append(2)
		if d2 < 4:
			a7 = 9*x
			a7 = a7*a7
			paths.append(3)
		else:
			x = x*4
			x = x+8
			a7 = 3+d2
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		a7 = d2**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))