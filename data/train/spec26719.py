import numpy as np 

def function(x):

	r4 = x
	n1 = x
	paths = []
	try:
		if x > 4:
			x = x*n1
			paths.append(1)
		else:
			n1 = n1+n1
			n1 = n1-n1
			r4 = r4-x
			paths.append(2)
		if r4 < 3:
			x = x+7
			paths.append(3)
		else:
			x = x/x
			x = x/5
			n1 = 8/n1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r4 = x**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))