import numpy as np 

def function(x):

	y4 = 4
	o6 = 6
	x = x
	paths = []
	try:
		if x >= 4:
			x = x+2
			o6 = x-o6
			o6 = 0-o6
			paths.append(1)
		else:
			o6 = o6+y4
			y4 = 5/1
			o6 = 5*o6
			paths.append(2)
		if o6 > 0:
			y4 = y4/8
			paths.append(3)
		else:
			y4 = 1+y4
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		x = o6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))