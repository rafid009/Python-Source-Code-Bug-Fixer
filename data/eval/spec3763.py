import numpy as np 

def function(x):

	n2 = x
	g3 = x
	paths = []
	try:
		if x > 0:
			x = 5*x
			paths.append(1)
		else:
			g3 = n2*n2
			paths.append(2)
		if x > 9:
			n2 = n2+9
			x = 5-g3
			paths.append(3)
		else:
			x = x*2
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