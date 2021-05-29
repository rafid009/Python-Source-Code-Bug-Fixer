import numpy as np 

def function(x):

	p8 = 0
	f3 = x
	x = x
	paths = []
	try:
		if p8 > 9:
			p8 = p8+3
			x = x+9
			paths.append(1)
		else:
			p8 = 7*p8
			f3 = 4-2
			x = x/9
			paths.append(2)
		if x > 7:
			x = x*x
			x = 9+x
			p8 = p8-1
			paths.append(3)
		else:
			p8 = p8*9
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