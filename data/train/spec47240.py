import numpy as np 

def function(x):

	p2 = x
	w4 = 7
	x = x
	paths = []
	try:
		if p2 > 5:
			w4 = x-w4
			paths.append(1)
		else:
			x = 8+x
			p2 = p2+8
			paths.append(2)
		if x > 3:
			p2 = 8*6
			p2 = 4-p2
			x = x+8
			paths.append(3)
		else:
			w4 = 5/w4
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		x = w4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))