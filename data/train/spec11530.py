import numpy as np 

def function(x):

	p8 = 6
	w1 = x
	paths = []
	try:
		if x <= 8:
			x = x/2
			w1 = w1-0
			x = x*5
			paths.append(1)
		else:
			w1 = p8+w1
			p8 = p8+7
			w1 = x/w1
			paths.append(2)
		if x < 3:
			x = x-4
			w1 = w1+7
			x = 6*x
			paths.append(3)
		else:
			w1 = 7-w1
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p8 = x**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))