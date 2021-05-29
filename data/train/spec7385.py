import numpy as np 

def function(x):

	p9 = 5
	a2 = x
	paths = []
	try:
		if x > 0:
			p9 = x/7
			p9 = 9+5
			x = 1-4
			paths.append(1)
		else:
			x = 2/5
			x = 4+1
			x = x/x
			paths.append(2)
		if x > 0:
			p9 = 3/p9
			x = x+8
			x = 0*x
			paths.append(3)
		else:
			p9 = p9+0
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))