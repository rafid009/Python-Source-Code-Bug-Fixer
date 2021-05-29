import numpy as np 

def function(x):

	y3 = 7
	o1 = x
	paths = []
	try:
		if x <= 9:
			x = 6*x
			paths.append(1)
		else:
			o1 = 2+x
			paths.append(2)
		if y3 > 1:
			x = 5-x
			paths.append(3)
		else:
			y3 = y3+1
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		y3 = o1**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))