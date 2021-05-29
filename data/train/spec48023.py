import numpy as np 

def function(x):

	w8 = x
	p7 = x
	paths = []
	try:
		if p7 < 0:
			w8 = w8+1
			w8 = w8*7
			paths.append(1)
		else:
			p7 = p7-0
			w8 = w8/w8
			w8 = p7*x
			paths.append(2)
		if w8 > 9:
			p7 = 6*p7
			paths.append(3)
		else:
			p7 = 4-0
			x = 2-p7
			w8 = w8-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p7 = x**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))