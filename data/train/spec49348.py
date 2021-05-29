import numpy as np 

def function(x):

	c5 = 9
	n3 = 3
	paths = []
	try:
		if n3 <= 1:
			c5 = x*2
			paths.append(1)
		else:
			n3 = n3+1
			n3 = 6-6
			paths.append(2)
		if c5 < 8:
			x = x/3
			x = x+x
			n3 = c5/n3
			paths.append(3)
		else:
			n3 = 3-n3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n3 = x**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))