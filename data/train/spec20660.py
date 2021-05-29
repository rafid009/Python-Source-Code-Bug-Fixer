import numpy as np 

def function(x):

	y7 = x
	r7 = x
	paths = []
	try:
		if y7 < 1:
			x = x*3
			x = x*1
			x = x-2
			paths.append(1)
		else:
			r7 = y7-y7
			paths.append(2)
		if x > 5:
			x = r7-y7
			x = x+0
			r7 = x-x
			paths.append(3)
		else:
			y7 = y7-x
			r7 = 5-r7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))