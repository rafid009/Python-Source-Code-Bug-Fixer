import numpy as np 

def function(x):

	b9 = x
	p9 = 8
	paths = []
	try:
		if b9 <= 4:
			p9 = 9-6
			x = 2/8
			paths.append(1)
		else:
			b9 = 9*b9
			p9 = p9-4
			b9 = 1/b9
			paths.append(2)
		if p9 < 2:
			b9 = b9*b9
			x = x*8
			x = 7/x
			paths.append(3)
		else:
			x = b9-5
			b9 = x/p9
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