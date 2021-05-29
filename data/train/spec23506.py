import numpy as np 

def function(x):

	e1 = 5
	p7 = 4
	paths = []
	try:
		if x <= 0:
			e1 = e1+x
			e1 = 0+5
			x = 7-x
			paths.append(1)
		else:
			x = p7-x
			e1 = e1*p7
			e1 = e1*2
			paths.append(2)
		if e1 > 7:
			p7 = p7*p7
			paths.append(3)
		else:
			p7 = 4*p7
			x = p7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p7 = x**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))