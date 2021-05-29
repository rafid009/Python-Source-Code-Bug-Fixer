import numpy as np 

def function(x):

	p9 = x
	e8 = 1
	paths = []
	try:
		if e8 <= 3:
			x = 7*x
			paths.append(1)
		else:
			p9 = p9*3
			e8 = e8-4
			x = x+9
			paths.append(2)
		if x <= 1:
			e8 = 1+3
			x = x/3
			paths.append(3)
		else:
			p9 = p9*2
			p9 = 3-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))