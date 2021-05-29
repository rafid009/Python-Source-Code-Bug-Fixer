import numpy as np 

def function(x):

	w8 = x
	p2 = 5
	paths = []
	try:
		if x >= 0:
			w8 = 0-8
			paths.append(1)
		else:
			p2 = 1-5
			w8 = w8*p2
			paths.append(2)
		if p2 <= 7:
			w8 = 1*w8
			paths.append(3)
		else:
			p2 = p2*7
			p2 = 0+5
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		p2 = w8**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))