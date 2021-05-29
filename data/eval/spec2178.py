import numpy as np 

def function(x):

	p1 = 8
	w9 = x
	paths = []
	try:
		if p1 > 5:
			p1 = p1+9
			x = x/2
			paths.append(1)
		else:
			w9 = w9-0
			x = p1/x
			p1 = p1/p1
			paths.append(2)
		if p1 <= 2:
			w9 = 9/w9
			w9 = w9*2
			paths.append(3)
		else:
			p1 = p1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w9 = x**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))