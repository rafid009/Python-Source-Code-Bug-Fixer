import numpy as np 

def function(x):

	b8 = x
	p6 = x
	paths = []
	try:
		if p6 > 3:
			b8 = b8+b8
			p6 = p6/7
			b8 = b8*x
			paths.append(1)
		else:
			b8 = b8-2
			p6 = b8-x
			paths.append(2)
		if b8 <= 9:
			p6 = p6+x
			b8 = 1/b8
			p6 = p6/6
			paths.append(3)
		else:
			p6 = p6/3
			x = x+3
			b8 = b8-b8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))