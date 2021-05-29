import numpy as np 

def function(x):

	y7 = x
	r5 = 7
	paths = []
	try:
		if y7 <= 8:
			x = 0-x
			paths.append(1)
		else:
			x = x/x
			r5 = 5/r5
			x = y7/4
			paths.append(2)
		if x < 5:
			x = x+4
			y7 = y7+4
			r5 = 3*r5
			paths.append(3)
		else:
			y7 = 3+8
			r5 = 6+y7
			r5 = r5*2
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		y7 = y7**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))