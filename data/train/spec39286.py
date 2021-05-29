import numpy as np 

def function(x):

	c7 = 6
	f3 = x
	paths = []
	try:
		if c7 > 9:
			c7 = 5+c7
			paths.append(1)
		else:
			c7 = c7-x
			paths.append(2)
		if f3 >= 4:
			c7 = c7*1
			x = f3+c7
			paths.append(3)
		else:
			f3 = f3-1
			c7 = c7/1
			c7 = x*c7
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		f3 = f3**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))