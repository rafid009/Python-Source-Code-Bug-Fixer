import numpy as np 

def function(x):

	o7 = x
	e1 = x
	paths = []
	try:
		if x > 9:
			e1 = e1*1
			e1 = o7/7
			e1 = o7-e1
			paths.append(1)
		else:
			o7 = x/4
			o7 = 6*5
			e1 = o7-e1
			paths.append(2)
		if o7 < 7:
			x = x*5
			e1 = e1/3
			x = x-x
			paths.append(3)
		else:
			x = x+x
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