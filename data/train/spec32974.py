import numpy as np 

def function(x):

	f7 = 7
	c1 = 2
	paths = []
	try:
		if c1 < 5:
			x = x+0
			c1 = c1*1
			f7 = f7-5
			paths.append(1)
		else:
			x = x-1
			paths.append(2)
		if x <= 0:
			c1 = c1/8
			c1 = c1-1
			f7 = 2+f7
			paths.append(3)
		else:
			f7 = 7/7
			c1 = c1*1
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		f7 = c1**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))