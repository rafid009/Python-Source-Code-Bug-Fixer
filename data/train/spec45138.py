import numpy as np 

def function(x):

	y3 = x
	n8 = 3
	x = 6
	paths = []
	try:
		if y3 <= 2:
			x = x*y3
			x = y3*7
			paths.append(1)
		else:
			y3 = 2*0
			n8 = 9+y3
			paths.append(2)
		if x >= 3:
			n8 = n8+3
			y3 = y3-2
			paths.append(3)
		else:
			x = x-2
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		n8 = y3**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))