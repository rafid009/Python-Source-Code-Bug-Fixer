import numpy as np 

def function(x):

	p8 = x
	w0 = 3
	paths = []
	try:
		if p8 > 2:
			x = x+8
			x = x+x
			x = 4-x
			paths.append(1)
		else:
			x = x/1
			x = x-4
			x = x+1
			paths.append(2)
		if x >= 0:
			x = x-4
			w0 = p8*3
			x = x/2
			paths.append(3)
		else:
			w0 = 0+4
			x = x+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p8 = x**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))