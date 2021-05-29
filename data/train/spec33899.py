import numpy as np 

def function(x):

	h9 = x
	p6 = x
	paths = []
	try:
		if h9 <= 5:
			p6 = 4+p6
			x = 6/7
			paths.append(1)
		else:
			p6 = 9-p6
			paths.append(2)
		if p6 < 7:
			p6 = p6*p6
			x = 3-7
			p6 = 3+p6
			paths.append(3)
		else:
			x = x-p6
			p6 = p6*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h9 = x**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))