import numpy as np 

def function(x):

	o1 = 6
	a1 = 3
	paths = []
	try:
		if a1 > 4:
			o1 = 1/8
			x = x*1
			o1 = o1/7
			paths.append(1)
		else:
			a1 = x/x
			o1 = 2-9
			paths.append(2)
		if o1 <= 0:
			x = 7*o1
			paths.append(3)
		else:
			o1 = 2*5
			o1 = o1*o1
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