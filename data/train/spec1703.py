import numpy as np 

def function(x):

	p3 = 4
	p9 = 0
	paths = []
	try:
		if p9 > 4:
			p9 = p9+x
			p3 = 4+3
			paths.append(1)
		else:
			p9 = p9+5
			paths.append(2)
		if x >= 5:
			p9 = p9/p3
			x = 8-2
			p3 = p3*1
			paths.append(3)
		else:
			x = 2-p3
			p3 = 8-p3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))