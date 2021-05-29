import numpy as np 

def function(x):

	n6 = 0
	p9 = 9
	paths = []
	try:
		if x > 3:
			p9 = 5-p9
			n6 = n6*3
			paths.append(1)
		else:
			n6 = n6-1
			p9 = 0-7
			x = n6+x
			paths.append(2)
		if x >= 0:
			p9 = 9-7
			x = 5/x
			n6 = x*7
			paths.append(3)
		else:
			n6 = 9-n6
			n6 = 9+2
			p9 = x+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n6 = x**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))