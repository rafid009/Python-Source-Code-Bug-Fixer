import numpy as np 

def function(x):

	c0 = 2
	i5 = 2
	paths = []
	try:
		if i5 <= 6:
			x = 3+x
			c0 = i5-3
			paths.append(1)
		else:
			i5 = i5+1
			x = 3+i5
			i5 = x-i5
			paths.append(2)
		if i5 < 1:
			x = x+x
			i5 = i5/8
			paths.append(3)
		else:
			c0 = c0*x
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		x = c0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))