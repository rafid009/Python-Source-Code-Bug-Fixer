import numpy as np 

def function(x):

	j7 = x
	d8 = x
	paths = []
	try:
		if d8 <= 5:
			j7 = 3/j7
			x = x*x
			paths.append(1)
		else:
			d8 = d8-1
			paths.append(2)
		if d8 >= 5:
			x = 6/8
			d8 = x*0
			paths.append(3)
		else:
			j7 = j7-d8
			x = j7/4
			d8 = 5*7
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