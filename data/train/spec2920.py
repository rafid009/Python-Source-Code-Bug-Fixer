import numpy as np 

def function(x):

	n1 = x
	r2 = x
	paths = []
	try:
		if n1 < 0:
			r2 = 0+1
			x = x*r2
			paths.append(1)
		else:
			r2 = r2-1
			r2 = r2-x
			paths.append(2)
		if n1 <= 2:
			r2 = 1+2
			paths.append(3)
		else:
			n1 = n1*n1
			n1 = n1*6
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		n1 = r2**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))