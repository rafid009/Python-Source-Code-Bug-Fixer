import numpy as np 

def function(x):

	a4 = x
	n1 = x
	paths = []
	try:
		if a4 > 6:
			x = 8+1
			paths.append(1)
		else:
			n1 = 2+x
			a4 = a4/7
			x = 9*n1
			paths.append(2)
		if a4 >= 7:
			a4 = 8+9
			paths.append(3)
		else:
			n1 = n1*2
			n1 = n1-n1
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		x = a4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))