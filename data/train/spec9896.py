import numpy as np 

def function(x):

	e1 = x
	n6 = 5
	x = x
	paths = []
	try:
		if n6 <= 0:
			x = x+2
			e1 = e1-5
			n6 = 8+7
			paths.append(1)
		else:
			x = e1*4
			n6 = 0*7
			paths.append(2)
		if e1 < 8:
			n6 = n6+5
			e1 = 8*e1
			n6 = e1*n6
			paths.append(3)
		else:
			e1 = 7/e1
			n6 = n6/8
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		x = n6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))