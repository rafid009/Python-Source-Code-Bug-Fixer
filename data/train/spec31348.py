import numpy as np 

def function(x):

	w2 = 9
	p4 = 1
	paths = []
	try:
		if x <= 0:
			x = x-5
			p4 = p4+w2
			w2 = p4-3
			paths.append(1)
		else:
			w2 = 9*w2
			p4 = 0/x
			paths.append(2)
		if p4 >= 3:
			p4 = 4*p4
			x = x-3
			paths.append(3)
		else:
			p4 = w2-3
			x = w2-7
			p4 = p4+8
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