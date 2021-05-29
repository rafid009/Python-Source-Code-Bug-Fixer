import numpy as np 

def function(x):

	g3 = x
	n6 = x
	paths = []
	try:
		if g3 <= 9:
			x = x*x
			x = x/9
			paths.append(1)
		else:
			x = 1+0
			x = 8+x
			n6 = 8+n6
			paths.append(2)
		if x > 6:
			x = 0*x
			n6 = n6*n6
			paths.append(3)
		else:
			n6 = n6*5
			g3 = g3/8
			n6 = g3-g3
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		n6 = g3**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))