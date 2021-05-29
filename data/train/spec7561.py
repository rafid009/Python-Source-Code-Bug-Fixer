import numpy as np 

def function(x):

	w8 = x
	c3 = x
	paths = []
	try:
		if c3 > 3:
			w8 = w8+5
			c3 = 3+c3
			x = x/6
			paths.append(1)
		else:
			x = x-c3
			x = x+x
			c3 = c3/3
			paths.append(2)
		if x <= 7:
			c3 = x-w8
			c3 = c3/2
			paths.append(3)
		else:
			x = x*w8
			x = x-7
			c3 = c3/9
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		w8 = c3**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))