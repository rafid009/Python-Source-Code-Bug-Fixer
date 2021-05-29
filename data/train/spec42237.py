import numpy as np 

def function(x):

	p9 = 2
	x3 = 3
	paths = []
	try:
		if x3 < 5:
			x = 6*x
			x3 = x-x3
			paths.append(1)
		else:
			p9 = p9*x3
			p9 = p9*7
			x3 = x3-p9
			paths.append(2)
		if p9 > 3:
			x3 = 0+4
			p9 = x+5
			p9 = x/x3
			paths.append(3)
		else:
			x = 9*6
			x = 7*p9
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x = x3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))