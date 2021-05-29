import numpy as np 

def function(x):

	p3 = x
	n6 = x
	paths = []
	try:
		if x >= 7:
			x = x-5
			p3 = 4/n6
			paths.append(1)
		else:
			p3 = x+p3
			paths.append(2)
		if n6 > 0:
			n6 = p3*8
			n6 = p3/x
			p3 = p3*5
			paths.append(3)
		else:
			x = 5*x
			x = x*3
			n6 = 7+x
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		x = n6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))