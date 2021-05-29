import numpy as np 

def function(x):

	p7 = x
	y3 = x
	paths = []
	try:
		if x < 7:
			y3 = 1+x
			p7 = p7-x
			paths.append(1)
		else:
			p7 = y3*x
			paths.append(2)
		if x <= 1:
			y3 = y3*y3
			y3 = x*y3
			y3 = 1-y3
			paths.append(3)
		else:
			y3 = 7*x
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