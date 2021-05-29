import numpy as np 

def function(x):

	p7 = 9
	w5 = 4
	paths = []
	try:
		if w5 < 6:
			x = 9-9
			paths.append(1)
		else:
			w5 = 9-w5
			p7 = 7/p7
			paths.append(2)
		if p7 > 2:
			p7 = p7+4
			w5 = w5/w5
			p7 = 6-p7
			paths.append(3)
		else:
			w5 = w5*5
			x = x+2
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		p7 = p7**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))