import numpy as np 

def function(x):

	l7 = x
	b2 = x
	paths = []
	try:
		if b2 >= 4:
			b2 = b2+1
			b2 = 1*b2
			paths.append(1)
		else:
			x = 2*x
			b2 = b2*b2
			b2 = b2/3
			paths.append(2)
		if l7 >= 4:
			b2 = l7*8
			paths.append(3)
		else:
			b2 = b2-8
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		x = l7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))