import numpy as np 

def function(x):

	w8 = x
	p4 = 6
	paths = []
	try:
		if p4 <= 7:
			w8 = w8-1
			paths.append(1)
		else:
			w8 = w8*8
			x = 2/x
			w8 = w8+w8
			paths.append(2)
		if p4 > 8:
			p4 = p4+9
			paths.append(3)
		else:
			w8 = w8-6
			w8 = w8/x
			p4 = p4+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p4 = x**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))