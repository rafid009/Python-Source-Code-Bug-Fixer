import numpy as np 

def function(x):

	w0 = 1
	p2 = x
	paths = []
	try:
		if x > 5:
			w0 = w0*w0
			paths.append(1)
		else:
			w0 = x+w0
			x = x+5
			paths.append(2)
		if p2 <= 0:
			p2 = p2+5
			w0 = 5/w0
			paths.append(3)
		else:
			p2 = x-x
			w0 = x+p2
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		p2 = w0**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))