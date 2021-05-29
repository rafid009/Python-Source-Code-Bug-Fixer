import numpy as np 

def function(x):

	n6 = 3
	n9 = x
	paths = []
	try:
		if n9 > 8:
			n6 = n6-x
			x = x*0
			paths.append(1)
		else:
			n9 = 2-n9
			paths.append(2)
		if n9 <= 1:
			n9 = x+7
			n6 = n9*x
			x = 3+0
			paths.append(3)
		else:
			n6 = 0-9
			x = 6/n6
			n9 = n9*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n6 = x**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))