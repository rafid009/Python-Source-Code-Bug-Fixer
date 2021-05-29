import numpy as np 

def function(x):

	v5 = 8
	n1 = x
	paths = []
	try:
		if x > 8:
			x = x-n1
			v5 = x-n1
			paths.append(1)
		else:
			v5 = v5/v5
			x = 9/n1
			paths.append(2)
		if v5 < 1:
			v5 = 2-v5
			n1 = x*n1
			v5 = v5-x
			paths.append(3)
		else:
			n1 = n1+8
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))