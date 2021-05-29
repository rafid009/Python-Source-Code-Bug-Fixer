import numpy as np 

def function(x):

	w0 = 8
	p9 = x
	paths = []
	try:
		if w0 < 8:
			w0 = w0/x
			x = x+x
			paths.append(1)
		else:
			x = p9*x
			p9 = p9-9
			paths.append(2)
		if p9 <= 3:
			w0 = 2+p9
			paths.append(3)
		else:
			w0 = p9-w0
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		p9 = w0**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))