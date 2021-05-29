import numpy as np 

def function(x):

	n4 = 1
	n2 = 5
	paths = []
	try:
		if x >= 7:
			x = x+n4
			paths.append(1)
		else:
			n2 = x/n2
			n4 = n4/5
			paths.append(2)
		if x > 5:
			n4 = x*2
			x = n4*x
			paths.append(3)
		else:
			n4 = n4+1
			x = x-3
			x = 8-8
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