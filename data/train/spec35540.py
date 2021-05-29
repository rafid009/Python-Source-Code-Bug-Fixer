import numpy as np 

def function(x):

	p0 = 4
	w3 = 3
	paths = []
	try:
		if w3 <= 7:
			w3 = p0-2
			p0 = p0/2
			paths.append(1)
		else:
			w3 = 3-p0
			w3 = p0+9
			x = 3-x
			paths.append(2)
		if p0 <= 7:
			w3 = x/w3
			p0 = p0+2
			paths.append(3)
		else:
			x = x/x
			x = x-1
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		p0 = w3**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))