import numpy as np 

def function(x):

	k7 = x
	p2 = 1
	paths = []
	try:
		if p2 <= 9:
			p2 = p2*p2
			paths.append(1)
		else:
			p2 = p2*x
			paths.append(2)
		if p2 >= 0:
			p2 = 8+x
			p2 = 1*p2
			paths.append(3)
		else:
			x = x+5
			k7 = k7/2
			p2 = p2+k7
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