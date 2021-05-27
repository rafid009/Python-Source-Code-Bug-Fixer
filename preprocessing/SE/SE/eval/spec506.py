import numpy as np 

def function(x):

	r6 = x
	c2 = 0
	paths = []
	try:
		if c2 <= 7:
			c2 = 2+x
			paths.append(1)
		else:
			c2 = 6-c2
			c2 = c2*2
			c2 = 0-c2
			paths.append(2)
		if r6 >= 8:
			x = 6-6
			paths.append(3)
		else:
			r6 = c2/c2
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		r6 = c2**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))