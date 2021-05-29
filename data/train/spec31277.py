import numpy as np 

def function(x):

	w1 = x
	n9 = x
	paths = []
	try:
		if x >= 4:
			w1 = n9*w1
			w1 = w1*w1
			paths.append(1)
		else:
			x = 9+6
			w1 = w1*9
			w1 = w1+7
			paths.append(2)
		if x < 7:
			n9 = 4+n9
			paths.append(3)
		else:
			n9 = 1+n9
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		n9 = w1**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))