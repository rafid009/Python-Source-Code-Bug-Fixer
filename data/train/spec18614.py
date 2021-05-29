import numpy as np 

def function(x):

	c6 = 6
	f8 = x
	paths = []
	try:
		if f8 < 9:
			x = 4*1
			paths.append(1)
		else:
			f8 = c6-f8
			paths.append(2)
		if x >= 9:
			f8 = 5/f8
			x = c6+6
			c6 = 3-c6
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		f8 = f8**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))