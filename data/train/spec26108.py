import numpy as np 

def function(x):

	h1 = x
	p9 = x
	paths = []
	try:
		if h1 < 5:
			h1 = h1+p9
			paths.append(1)
		else:
			h1 = 3+x
			paths.append(2)
		if x > 3:
			p9 = 6*9
			p9 = 4/3
			x = x+7
			paths.append(3)
		else:
			p9 = 5*h1
			h1 = 6+h1
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