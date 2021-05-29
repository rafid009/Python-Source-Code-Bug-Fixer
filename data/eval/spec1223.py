import numpy as np 

def function(x):

	x1 = x
	o5 = x
	paths = []
	try:
		if x > 7:
			o5 = o5-8
			x = 7+x1
			paths.append(1)
		else:
			o5 = 8+1
			x = x+8
			x = 1-2
			paths.append(2)
		if x >= 2:
			x = x1+1
			x1 = x1+4
			paths.append(3)
		else:
			x = x-2
			x = 1/9
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		x1 = o5**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))