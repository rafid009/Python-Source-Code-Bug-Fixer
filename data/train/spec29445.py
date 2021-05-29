import numpy as np 

def function(x):

	c3 = x
	f0 = 6
	paths = []
	try:
		if f0 > 9:
			f0 = f0/9
			c3 = c3*x
			c3 = c3-1
			paths.append(1)
		else:
			x = x/3
			x = 1-5
			paths.append(2)
		if x < 5:
			x = 0+x
			x = c3*4
			f0 = f0/6
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		f0 = c3**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))