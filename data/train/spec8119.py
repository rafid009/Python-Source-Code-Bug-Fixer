import numpy as np 

def function(x):

	w4 = x
	p2 = x
	x = 1
	paths = []
	try:
		if w4 >= 6:
			w4 = 1*w4
			x = 3-x
			paths.append(1)
		else:
			w4 = 8/w4
			x = 7+w4
			paths.append(2)
		if p2 <= 3:
			x = x+2
			w4 = 4-w4
			paths.append(3)
		else:
			x = x/6
			x = 9*x
			p2 = 9*p2
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		w4 = p2**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))