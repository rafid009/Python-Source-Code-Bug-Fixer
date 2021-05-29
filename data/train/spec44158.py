import numpy as np 

def function(x):

	e4 = x
	o1 = x
	paths = []
	try:
		if e4 <= 1:
			o1 = o1/5
			x = 3/x
			x = 7/o1
			paths.append(1)
		else:
			x = 6-x
			paths.append(2)
		if e4 < 5:
			x = 2+4
			o1 = x/x
			e4 = o1*e4
			paths.append(3)
		else:
			x = 8*x
			o1 = 3/9
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		o1 = e4**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))