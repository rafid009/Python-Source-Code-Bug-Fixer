import numpy as np 

def function(x):

	y3 = 6
	n1 = x
	paths = []
	try:
		if y3 <= 1:
			n1 = n1-3
			n1 = 2/5
			y3 = y3*1
			paths.append(1)
		else:
			n1 = 4-n1
			y3 = y3+x
			paths.append(2)
		if y3 < 7:
			n1 = 6-6
			x = x/x
			x = x+x
			paths.append(3)
		else:
			y3 = y3/x
			n1 = y3*n1
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		n1 = y3**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))