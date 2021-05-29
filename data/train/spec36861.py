import numpy as np 

def function(x):

	c2 = 0
	u5 = x
	paths = []
	try:
		if u5 <= 7:
			u5 = 1/6
			c2 = x*9
			paths.append(1)
		else:
			u5 = 1*0
			u5 = u5-3
			x = x+4
			paths.append(2)
		if u5 > 7:
			c2 = c2/9
			x = u5*4
			paths.append(3)
		else:
			u5 = u5+4
			u5 = 5+u5
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