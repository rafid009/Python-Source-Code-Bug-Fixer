import numpy as np 

def function(x):

	v0 = x
	n1 = x
	x = x
	paths = []
	try:
		if n1 < 2:
			x = n1/x
			x = x+7
			paths.append(1)
		else:
			n1 = 3+n1
			x = x*4
			paths.append(2)
		if n1 <= 0:
			x = x-x
			x = 5/n1
			paths.append(3)
		else:
			v0 = v0/3
			x = 9*1
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		x = v0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))