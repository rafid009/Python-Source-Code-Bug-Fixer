import numpy as np 

def function(x):

	p0 = 2
	w7 = x
	paths = []
	try:
		if x > 4:
			x = x+6
			p0 = p0-3
			x = w7+p0
			paths.append(1)
		else:
			x = x+5
			w7 = w7-3
			paths.append(2)
		if x < 3:
			p0 = p0+3
			w7 = 0/4
			paths.append(3)
		else:
			w7 = x+w7
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		p0 = w7**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))