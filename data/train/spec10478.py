import numpy as np 

def function(x):

	o1 = 8
	y7 = 3
	paths = []
	try:
		if o1 >= 3:
			o1 = o1-x
			o1 = o1/o1
			paths.append(1)
		else:
			y7 = y7+5
			y7 = o1+9
			paths.append(2)
		if o1 >= 8:
			x = x*6
			y7 = 5-y7
			o1 = x*9
			paths.append(3)
		else:
			o1 = 2/5
			o1 = o1+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))