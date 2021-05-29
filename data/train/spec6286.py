import numpy as np 

def function(x):

	n1 = 4
	y4 = x
	paths = []
	try:
		if n1 >= 4:
			x = x/7
			n1 = 0-n1
			paths.append(1)
		else:
			n1 = n1+x
			x = 2-9
			paths.append(2)
		if y4 >= 1:
			x = n1-7
			n1 = n1*5
			paths.append(3)
		else:
			y4 = y4+4
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		y4 = n1**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))