import numpy as np 

def function(x):

	x7 = x
	p1 = 9
	paths = []
	try:
		if x < 3:
			x = x-x7
			paths.append(1)
		else:
			x7 = p1+x7
			p1 = 3/p1
			paths.append(2)
		if x <= 7:
			p1 = p1+0
			x = 1*x
			paths.append(3)
		else:
			x7 = x+1
			p1 = x7+x
			x7 = x7-p1
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x = x7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))