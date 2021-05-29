import numpy as np 

def function(x):

	x1 = x
	o1 = x
	paths = []
	try:
		if x > 0:
			x1 = x1*2
			paths.append(1)
		else:
			o1 = o1/3
			x1 = x1*1
			paths.append(2)
		if x >= 8:
			x = 0/x1
			o1 = 1*5
			o1 = o1+7
			paths.append(3)
		else:
			x1 = x+8
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		x1 = o1**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))