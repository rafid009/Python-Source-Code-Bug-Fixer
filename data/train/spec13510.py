import numpy as np 

def function(x):

	b2 = 9
	p7 = 0
	paths = []
	try:
		if b2 > 2:
			b2 = 8+p7
			b2 = x*b2
			paths.append(1)
		else:
			b2 = b2-b2
			p7 = 1*0
			paths.append(2)
		if b2 > 5:
			x = 2-x
			p7 = p7+4
			x = 5-x
			paths.append(3)
		else:
			p7 = p7+x
			b2 = b2-9
			b2 = b2*2
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))