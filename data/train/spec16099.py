import numpy as np 

def function(x):

	l6 = 6
	p7 = 7
	paths = []
	try:
		if l6 < 5:
			p7 = 6+p7
			p7 = p7/4
			paths.append(1)
		else:
			p7 = l6*p7
			x = 2*x
			p7 = p7+p7
			paths.append(2)
		if p7 >= 2:
			p7 = p7/9
			p7 = p7-x
			paths.append(3)
		else:
			l6 = l6+1
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