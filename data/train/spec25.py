import numpy as np 

def function(x):

	y7 = 4
	r5 = x
	paths = []
	try:
		if y7 <= 1:
			y7 = y7*0
			x = 1-7
			paths.append(1)
		else:
			r5 = r5*3
			y7 = 0/y7
			paths.append(2)
		if y7 <= 0:
			y7 = 5+y7
			y7 = y7+r5
			paths.append(3)
		else:
			r5 = r5/x
			r5 = r5-3
			y7 = 8-y7
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		x = y7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))