import numpy as np 

def function(x):

	i9 = 5
	p9 = x
	x = x
	paths = []
	try:
		if i9 > 7:
			i9 = 3+i9
			p9 = 0/x
			paths.append(1)
		else:
			x = x-i9
			i9 = i9*8
			p9 = 2/x
			paths.append(2)
		if i9 > 9:
			x = p9+p9
			i9 = i9-7
			paths.append(3)
		else:
			x = x/p9
			x = i9*1
			x = 4*x
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