import numpy as np 

def function(x):

	b4 = x
	p7 = 5
	paths = []
	try:
		if b4 >= 3:
			x = x*2
			x = 7-x
			paths.append(1)
		else:
			x = x-2
			b4 = 9+p7
			b4 = 5+b4
			paths.append(2)
		if p7 <= 7:
			p7 = b4+3
			p7 = x/p7
			paths.append(3)
		else:
			p7 = p7+p7
			x = 8+x
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