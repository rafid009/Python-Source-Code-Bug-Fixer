import numpy as np 

def function(x):

	n1 = 5
	y3 = x
	paths = []
	try:
		if n1 <= 2:
			y3 = y3+8
			n1 = n1-4
			paths.append(1)
		else:
			x = y3/x
			y3 = 6+y3
			paths.append(2)
		if y3 >= 2:
			n1 = x/n1
			y3 = n1/x
			paths.append(3)
		else:
			x = 7*x
			y3 = x/y3
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		y3 = y3**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))