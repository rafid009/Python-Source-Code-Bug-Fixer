import numpy as np 

def function(x):

	x2 = x
	d6 = 5
	paths = []
	try:
		if x >= 1:
			d6 = d6*2
			x = x*9
			paths.append(1)
		else:
			d6 = 1+x
			x = x/x
			paths.append(2)
		if x > 8:
			d6 = d6/1
			x2 = x2-5
			paths.append(3)
		else:
			x2 = 9*x2
			d6 = d6/x2
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x2 = x2**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))