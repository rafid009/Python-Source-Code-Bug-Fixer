import numpy as np 

def function(x):

	p2 = 1
	i6 = x
	paths = []
	try:
		if p2 < 6:
			p2 = 5-p2
			paths.append(1)
		else:
			x = 1*x
			i6 = 5+4
			paths.append(2)
		if x <= 4:
			x = x/7
			p2 = x+p2
			p2 = 7*x
			paths.append(3)
		else:
			p2 = 5*p2
			x = x-p2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))