import numpy as np 

def function(x):

	o4 = 8
	o1 = x
	paths = []
	try:
		if x < 6:
			x = 0+6
			x = o1-x
			paths.append(1)
		else:
			x = 5+1
			paths.append(2)
		if o4 > 7:
			o1 = 4*9
			o1 = 3-o4
			o4 = o4*5
			paths.append(3)
		else:
			o1 = 1*6
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		x = o1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))