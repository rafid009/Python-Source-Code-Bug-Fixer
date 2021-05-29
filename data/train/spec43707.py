import numpy as np 

def function(x):

	x6 = 0
	d2 = 3
	paths = []
	try:
		if x <= 2:
			d2 = 5+2
			x6 = 6+3
			paths.append(1)
		else:
			x = x+7
			x6 = x*x6
			x = d2-x
			paths.append(2)
		if x < 0:
			d2 = x6*d2
			x = x-3
			x6 = x6-5
			paths.append(3)
		else:
			x = 7+x
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		d2 = x6**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))