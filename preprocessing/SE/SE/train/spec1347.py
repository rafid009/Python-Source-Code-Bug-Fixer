import numpy as np 

def function(x):

	y2 = 9
	n2 = x
	paths = []
	try:
		if y2 > 1:
			x = 2*x
			n2 = n2*6
			paths.append(1)
		else:
			y2 = 0+y2
			n2 = 0+4
			x = n2+7
			paths.append(2)
		if n2 >= 5:
			y2 = 1+x
			n2 = n2-y2
			paths.append(3)
		else:
			x = x+8
			x = 6+x
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