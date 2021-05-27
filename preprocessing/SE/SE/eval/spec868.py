import numpy as np 

def function(x):

	v1 = x
	p7 = x
	x = x
	paths = []
	try:
		if p7 <= 6:
			x = x*7
			paths.append(1)
		else:
			p7 = p7-v1
			paths.append(2)
		if p7 >= 7:
			p7 = p7*8
			p7 = 7+p7
			p7 = 6+p7
			paths.append(3)
		else:
			v1 = v1-1
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