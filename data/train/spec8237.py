import numpy as np 

def function(x):

	i1 = x
	p7 = x
	paths = []
	try:
		if x < 4:
			i1 = 8/i1
			p7 = p7-p7
			i1 = 6+i1
			paths.append(1)
		else:
			i1 = x+p7
			p7 = p7*p7
			p7 = 1+p7
			paths.append(2)
		if p7 > 7:
			x = x+2
			x = 8+x
			x = 7+5
			paths.append(3)
		else:
			i1 = i1/x
			p7 = 4-i1
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