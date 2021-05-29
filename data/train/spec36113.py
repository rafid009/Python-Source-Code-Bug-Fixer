import numpy as np 

def function(x):

	o1 = 3
	o8 = 9
	paths = []
	try:
		if o1 >= 3:
			o1 = 4-o1
			o8 = 2+o8
			paths.append(1)
		else:
			o8 = o8*o8
			o8 = o8*0
			o1 = o1+6
			paths.append(2)
		if o8 < 3:
			x = 4/x
			paths.append(3)
		else:
			x = x/1
			o8 = o1+7
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