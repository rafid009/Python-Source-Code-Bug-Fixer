import numpy as np 

def function(x):

	p9 = x
	b5 = 0
	paths = []
	try:
		if p9 >= 2:
			x = 1/x
			x = x*7
			p9 = p9/1
			paths.append(1)
		else:
			p9 = 6/p9
			b5 = 3-7
			p9 = 2*p9
			paths.append(2)
		if b5 <= 8:
			p9 = 4+9
			b5 = b5*8
			p9 = p9*b5
			paths.append(3)
		else:
			x = 3*7
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		x = b5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))