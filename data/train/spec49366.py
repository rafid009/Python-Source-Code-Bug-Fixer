import numpy as np 

def function(x):

	p7 = 0
	a4 = x
	paths = []
	try:
		if a4 <= 4:
			a4 = a4*2
			a4 = a4+2
			a4 = 2-6
			paths.append(1)
		else:
			p7 = 8*p7
			x = a4-x
			p7 = p7/3
			paths.append(2)
		if x < 2:
			p7 = a4+0
			x = 3*x
			paths.append(3)
		else:
			a4 = a4+9
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