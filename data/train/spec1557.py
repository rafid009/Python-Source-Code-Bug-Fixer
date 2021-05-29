import numpy as np 

def function(x):

	j5 = x
	p9 = 1
	paths = []
	try:
		if p9 >= 9:
			j5 = j5-8
			x = 2/j5
			paths.append(1)
		else:
			p9 = p9+j5
			x = p9*x
			paths.append(2)
		if p9 > 0:
			p9 = 7-3
			p9 = 0-3
			p9 = p9*5
			paths.append(3)
		else:
			j5 = 0-j5
			p9 = p9/6
			p9 = p9/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p9 = x**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))