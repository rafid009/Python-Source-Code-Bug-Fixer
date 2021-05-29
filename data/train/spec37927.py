import numpy as np 

def function(x):

	c5 = x
	f6 = 8
	paths = []
	try:
		if x < 8:
			c5 = f6*c5
			paths.append(1)
		else:
			x = x*x
			x = x+3
			paths.append(2)
		if c5 < 3:
			f6 = x/f6
			f6 = f6+c5
			c5 = c5+8
			paths.append(3)
		else:
			f6 = f6*7
			x = x*1
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		f6 = c5**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))