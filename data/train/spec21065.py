import numpy as np 

def function(x):

	p5 = x
	n6 = 8
	paths = []
	try:
		if x <= 1:
			p5 = p5-1
			paths.append(1)
		else:
			p5 = 9+p5
			n6 = 7+n6
			paths.append(2)
		if p5 > 0:
			x = x-7
			n6 = 9*n6
			paths.append(3)
		else:
			n6 = 0+n6
			n6 = 7*0
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