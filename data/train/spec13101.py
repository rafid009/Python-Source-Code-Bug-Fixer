import numpy as np 

def function(x):

	b3 = x
	p2 = x
	paths = []
	try:
		if x > 8:
			x = x*5
			paths.append(1)
		else:
			b3 = 3/b3
			p2 = p2-6
			paths.append(2)
		if b3 >= 5:
			x = 0-x
			x = p2*x
			b3 = 1+0
			paths.append(3)
		else:
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		b3 = p2**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))