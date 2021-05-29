import numpy as np 

def function(x):

	n1 = 0
	r2 = x
	paths = []
	try:
		if x >= 4:
			r2 = r2+n1
			n1 = 0*7
			paths.append(1)
		else:
			r2 = 0+r2
			n1 = r2+8
			paths.append(2)
		if r2 > 9:
			x = 7*x
			r2 = r2*x
			paths.append(3)
		else:
			r2 = x*1
			x = x-r2
			x = x-x
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		r2 = n1**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))