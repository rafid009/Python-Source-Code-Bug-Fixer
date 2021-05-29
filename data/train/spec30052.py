import numpy as np 

def function(x):

	p6 = x
	r9 = 8
	paths = []
	try:
		if p6 <= 3:
			r9 = x+5
			paths.append(1)
		else:
			p6 = 2/x
			x = 9-p6
			paths.append(2)
		if r9 <= 9:
			r9 = r9/6
			x = x+p6
			x = x*8
			paths.append(3)
		else:
			x = 2+x
			x = x/x
			r9 = p6-x
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