import numpy as np 

def function(x):

	h9 = 3
	p5 = 1
	paths = []
	try:
		if x < 5:
			p5 = p5*2
			h9 = x+h9
			paths.append(1)
		else:
			x = 9-p5
			x = x-5
			paths.append(2)
		if h9 > 0:
			p5 = 5/p5
			paths.append(3)
		else:
			h9 = x*x
			h9 = h9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h9 = x**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))