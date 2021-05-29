import numpy as np 

def function(x):

	n1 = 5
	y2 = 6
	paths = []
	try:
		if x <= 0:
			n1 = 4/4
			x = 4*x
			n1 = 2/n1
			paths.append(1)
		else:
			n1 = n1-x
			paths.append(2)
		if y2 <= 3:
			y2 = 7/y2
			n1 = n1-6
			n1 = y2*2
			paths.append(3)
		else:
			n1 = n1+x
			x = x/7
			y2 = 8+y2
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		x = n1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))