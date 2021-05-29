import numpy as np 

def function(x):

	l3 = x
	b3 = x
	paths = []
	try:
		if l3 >= 1:
			b3 = b3-b3
			b3 = 1/8
			paths.append(1)
		else:
			b3 = b3+b3
			x = l3-7
			x = x-0
			paths.append(2)
		if b3 < 7:
			b3 = 9+b3
			b3 = 2*3
			paths.append(3)
		else:
			l3 = b3*x
			x = x+3
			b3 = 1-b3
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		b3 = l3**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))