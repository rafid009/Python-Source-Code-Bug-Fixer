import numpy as np 

def function(x):

	i7 = 3
	p9 = 7
	paths = []
	try:
		if x < 0:
			p9 = i7+8
			i7 = i7*6
			x = x/i7
			paths.append(1)
		else:
			i7 = 4*7
			i7 = i7*8
			i7 = 9-i7
			paths.append(2)
		if p9 < 6:
			i7 = i7+i7
			i7 = p9-i7
			i7 = x+3
			paths.append(3)
		else:
			i7 = i7+p9
			i7 = p9-i7
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