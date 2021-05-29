import numpy as np 

def function(x):

	k4 = x
	d6 = 2
	paths = []
	try:
		if k4 >= 1:
			k4 = k4-8
			k4 = 5/k4
			paths.append(1)
		else:
			k4 = d6/7
			x = x/k4
			paths.append(2)
		if x <= 7:
			d6 = d6+7
			x = x-0
			paths.append(3)
		else:
			x = x+8
			d6 = x*3
			d6 = k4/6
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