import numpy as np 

def function(x):

	v7 = x
	p9 = x
	paths = []
	try:
		if v7 >= 4:
			p9 = 7/8
			paths.append(1)
		else:
			x = 8+x
			x = 5*x
			paths.append(2)
		if v7 >= 3:
			x = x/v7
			x = x*8
			paths.append(3)
		else:
			p9 = p9+8
			v7 = v7+3
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