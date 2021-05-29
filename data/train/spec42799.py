import numpy as np 

def function(x):

	r6 = x
	c2 = x
	paths = []
	try:
		if r6 <= 2:
			c2 = c2*6
			paths.append(1)
		else:
			r6 = r6+x
			paths.append(2)
		if c2 > 0:
			r6 = 2+7
			r6 = r6/2
			x = x+5
			paths.append(3)
		else:
			c2 = x*2
			x = x/2
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