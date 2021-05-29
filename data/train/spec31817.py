import numpy as np 

def function(x):

	p7 = x
	w1 = 0
	paths = []
	try:
		if x <= 4:
			p7 = x+2
			paths.append(1)
		else:
			w1 = p7-6
			paths.append(2)
		if x <= 4:
			x = p7*5
			w1 = w1+4
			x = x+2
			paths.append(3)
		else:
			p7 = 8+7
			x = x+9
			x = x-p7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))