import numpy as np 

def function(x):

	u6 = 2
	n2 = 9
	paths = []
	try:
		if u6 <= 8:
			n2 = 2-1
			u6 = n2-u6
			paths.append(1)
		else:
			n2 = 3-8
			paths.append(2)
		if x >= 1:
			u6 = x*x
			u6 = 3+u6
			paths.append(3)
		else:
			u6 = u6+4
			u6 = 1-4
			n2 = 3*u6
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