import numpy as np 

def function(x):

	w1 = 3
	p2 = x
	paths = []
	try:
		if w1 > 4:
			w1 = w1*5
			p2 = w1*p2
			paths.append(1)
		else:
			x = 0-6
			x = x-3
			paths.append(2)
		if w1 < 5:
			w1 = w1*7
			w1 = w1+5
			paths.append(3)
		else:
			w1 = 5*w1
			p2 = 2+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))