import numpy as np 

def function(x):

	c2 = x
	f5 = 3
	x = 3
	paths = []
	try:
		if c2 > 3:
			x = x*x
			x = x-9
			c2 = 7*1
			paths.append(1)
		else:
			f5 = f5*c2
			f5 = f5+2
			f5 = 7-f5
			paths.append(2)
		if c2 < 3:
			f5 = 3/f5
			paths.append(3)
		else:
			c2 = 2/f5
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		f5 = c2**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))