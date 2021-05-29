import numpy as np 

def function(x):

	v5 = 9
	p7 = 2
	paths = []
	try:
		if x > 7:
			x = x+2
			paths.append(1)
		else:
			x = 0+x
			p7 = p7/4
			p7 = 5/p7
			paths.append(2)
		if v5 <= 9:
			v5 = 5*v5
			paths.append(3)
		else:
			v5 = 4+4
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