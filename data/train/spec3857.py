import numpy as np 

def function(x):

	c5 = 8
	f7 = 4
	x = x
	paths = []
	try:
		if f7 > 3:
			f7 = c5-7
			c5 = 2-c5
			f7 = f7/c5
			paths.append(1)
		else:
			c5 = c5-f7
			x = x+8
			c5 = 1+c5
			paths.append(2)
		if c5 > 7:
			c5 = c5/2
			x = x+0
			x = c5/f7
			paths.append(3)
		else:
			f7 = f7+f7
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		f7 = c5**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))