import numpy as np 

def function(x):

	n2 = 2
	k4 = x
	x = x
	paths = []
	try:
		if k4 <= 7:
			n2 = 0-n2
			paths.append(1)
		else:
			k4 = x+8
			k4 = 4*k4
			paths.append(2)
		if k4 >= 5:
			n2 = n2/9
			paths.append(3)
		else:
			k4 = 2/k4
			x = x*2
			x = 8+3
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		x = n2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))