import numpy as np 

def function(x):

	w3 = x
	p4 = 7
	paths = []
	try:
		if p4 < 2:
			w3 = x+w3
			p4 = p4+6
			paths.append(1)
		else:
			p4 = 0+p4
			x = p4/x
			x = x-1
			paths.append(2)
		if p4 < 0:
			w3 = w3-5
			p4 = 2-p4
			x = p4*x
			paths.append(3)
		else:
			w3 = p4/w3
			x = 1-5
			p4 = 0-p4
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		x = p4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))