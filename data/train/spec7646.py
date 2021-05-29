import numpy as np 

def function(x):

	c6 = x
	f4 = 7
	paths = []
	try:
		if f4 > 7:
			x = x*1
			c6 = 1/f4
			paths.append(1)
		else:
			x = 8/6
			c6 = 9*c6
			x = 4-x
			paths.append(2)
		if f4 < 5:
			x = c6+x
			paths.append(3)
		else:
			x = x*3
			c6 = c6/3
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		f4 = c6**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))