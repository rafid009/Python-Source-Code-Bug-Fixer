import numpy as np 

def function(x):

	n1 = 7
	r9 = x
	paths = []
	try:
		if n1 <= 2:
			r9 = 3+r9
			paths.append(1)
		else:
			x = 8-x
			paths.append(2)
		if r9 <= 8:
			n1 = r9/8
			paths.append(3)
		else:
			n1 = 5+n1
			n1 = n1/7
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		r9 = n1**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))