import numpy as np 

def function(x):

	p4 = x
	w8 = 9
	paths = []
	try:
		if p4 >= 9:
			w8 = w8-w8
			w8 = w8+p4
			paths.append(1)
		else:
			w8 = w8-7
			w8 = w8/p4
			paths.append(2)
		if x <= 2:
			w8 = w8-2
			x = x/1
			x = 3+x
			paths.append(3)
		else:
			p4 = w8+3
			p4 = p4+x
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