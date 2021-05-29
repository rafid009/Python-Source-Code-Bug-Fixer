import numpy as np 

def function(x):

	p9 = x
	b4 = x
	paths = []
	try:
		if b4 < 3:
			x = b4/9
			b4 = b4*x
			p9 = 2-p9
			paths.append(1)
		else:
			b4 = p9*4
			paths.append(2)
		if b4 <= 0:
			b4 = 1+4
			paths.append(3)
		else:
			p9 = x+b4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p9 = x**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))