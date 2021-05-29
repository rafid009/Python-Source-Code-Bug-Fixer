import numpy as np 

def function(x):

	p9 = 2
	x7 = x
	paths = []
	try:
		if x7 <= 0:
			x7 = x7-1
			x = x7*p9
			x7 = p9-9
			paths.append(1)
		else:
			p9 = p9*0
			paths.append(2)
		if p9 <= 7:
			x7 = x7*6
			x7 = 8+x
			x = p9*x
			paths.append(3)
		else:
			x = p9+7
			p9 = 1/p9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x7 = x**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))