import numpy as np 

def function(x):

	o8 = x
	r1 = x
	paths = []
	try:
		if x < 8:
			x = x/r1
			paths.append(1)
		else:
			x = 3+7
			paths.append(2)
		if x <= 6:
			x = 8*o8
			x = 7-o8
			x = x/8
			paths.append(3)
		else:
			r1 = 1/r1
			r1 = r1/r1
			x = x+x
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		o8 = o8**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))