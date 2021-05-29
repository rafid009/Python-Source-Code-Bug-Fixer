import numpy as np 

def function(x):

	b2 = x
	p8 = x
	paths = []
	try:
		if b2 > 4:
			b2 = p8*b2
			paths.append(1)
		else:
			b2 = 2/4
			b2 = b2/x
			paths.append(2)
		if b2 > 4:
			x = x*x
			x = 6/x
			b2 = 0/b2
			paths.append(3)
		else:
			x = 1*0
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		p8 = b2**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))