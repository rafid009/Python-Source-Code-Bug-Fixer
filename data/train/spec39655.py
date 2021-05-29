import numpy as np 

def function(x):

	w3 = 3
	p6 = 5
	paths = []
	try:
		if w3 < 9:
			w3 = p6+5
			x = 7-x
			p6 = p6+p6
			paths.append(1)
		else:
			w3 = 2+6
			x = 3*p6
			p6 = w3*6
			paths.append(2)
		if w3 > 4:
			x = 0+x
			p6 = 3*1
			w3 = p6+w3
			paths.append(3)
		else:
			x = 1*x
			p6 = 6-0
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