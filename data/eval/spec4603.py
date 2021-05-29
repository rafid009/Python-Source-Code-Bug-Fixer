import numpy as np 

def function(x):

	i5 = x
	p8 = x
	x = 9
	paths = []
	try:
		if i5 < 7:
			x = 4-x
			paths.append(1)
		else:
			x = x/7
			x = i5+6
			x = x*2
			paths.append(2)
		if i5 < 3:
			x = 2*i5
			p8 = p8/i5
			paths.append(3)
		else:
			x = p8-0
			p8 = p8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p8 = x**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))