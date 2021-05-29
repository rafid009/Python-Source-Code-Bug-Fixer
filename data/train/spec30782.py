import numpy as np 

def function(x):

	o1 = x
	y2 = 5
	paths = []
	try:
		if o1 > 6:
			x = 2*9
			x = x/4
			x = x/5
			paths.append(1)
		else:
			x = x/8
			x = x-6
			paths.append(2)
		if o1 <= 1:
			y2 = y2/o1
			paths.append(3)
		else:
			y2 = o1+6
			x = x/y2
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		y2 = o1**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))