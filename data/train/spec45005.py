import numpy as np 

def function(x):

	n5 = 2
	y5 = 9
	paths = []
	try:
		if x < 0:
			n5 = n5*8
			n5 = n5+y5
			x = 5/x
			paths.append(1)
		else:
			n5 = n5/n5
			n5 = x*3
			paths.append(2)
		if y5 > 4:
			x = n5*x
			y5 = 2/y5
			x = 4+x
			paths.append(3)
		else:
			y5 = 4-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y5 = x**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))