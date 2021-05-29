import numpy as np 

def function(x):

	p4 = x
	w2 = 9
	paths = []
	try:
		if w2 <= 9:
			w2 = w2-w2
			paths.append(1)
		else:
			x = x-w2
			p4 = 1/6
			p4 = x-4
			paths.append(2)
		if w2 < 2:
			x = x/9
			p4 = 6+p4
			w2 = x-5
			paths.append(3)
		else:
			p4 = p4*5
			p4 = x-4
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		p4 = p4**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))