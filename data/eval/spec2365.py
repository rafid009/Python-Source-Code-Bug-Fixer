import numpy as np 

def function(x):

	c0 = 4
	f0 = x
	paths = []
	try:
		if c0 <= 4:
			c0 = c0*8
			c0 = 7-2
			paths.append(1)
		else:
			f0 = f0-7
			f0 = f0+x
			paths.append(2)
		if x > 6:
			f0 = 0*3
			c0 = f0-2
			paths.append(3)
		else:
			c0 = f0/c0
			f0 = 1/7
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		f0 = c0**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))