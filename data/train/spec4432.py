import numpy as np 

def function(x):

	a3 = 5
	b0 = x
	paths = []
	try:
		if a3 > 6:
			x = a3-a3
			x = x/6
			a3 = 8+a3
			paths.append(1)
		else:
			b0 = b0+3
			paths.append(2)
		if x < 6:
			b0 = 2*b0
			b0 = 6*5
			a3 = a3-6
			paths.append(3)
		else:
			b0 = x/b0
			a3 = 1*a3
			b0 = b0*a3
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		a3 = a3**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))