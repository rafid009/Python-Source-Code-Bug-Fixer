import numpy as np 

def function(x):

	n8 = 9
	w1 = x
	x = x
	paths = []
	try:
		if x <= 6:
			n8 = w1*n8
			paths.append(1)
		else:
			x = 2+n8
			x = x/2
			x = x+7
			paths.append(2)
		if w1 >= 3:
			w1 = w1-0
			paths.append(3)
		else:
			x = w1/4
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		n8 = w1**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))