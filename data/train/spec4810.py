import numpy as np 

def function(x):

	w2 = 5
	p1 = 6
	paths = []
	try:
		if p1 > 2:
			w2 = 5*w2
			w2 = 6/6
			w2 = 5*x
			paths.append(1)
		else:
			w2 = w2/w2
			p1 = 4+3
			paths.append(2)
		if x > 8:
			p1 = p1/p1
			w2 = p1/w2
			w2 = 5*w2
			paths.append(3)
		else:
			p1 = 3/p1
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		p1 = w2**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))