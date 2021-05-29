import numpy as np 

def function(x):

	o5 = x
	y8 = x
	x = 1
	paths = []
	try:
		if y8 <= 3:
			y8 = x*3
			paths.append(1)
		else:
			x = x+4
			y8 = 1*y8
			paths.append(2)
		if y8 <= 5:
			y8 = y8*o5
			y8 = 7*y8
			o5 = o5/3
			paths.append(3)
		else:
			y8 = 5*x
			y8 = y8/4
			y8 = o5/x
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		y8 = y8**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))