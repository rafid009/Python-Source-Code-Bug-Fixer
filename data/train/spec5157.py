import numpy as np 

def function(x):

	c8 = x
	w8 = 3
	paths = []
	try:
		if x >= 8:
			w8 = w8-5
			paths.append(1)
		else:
			c8 = 5*c8
			c8 = w8*0
			c8 = 9+x
			paths.append(2)
		if x <= 6:
			w8 = w8-0
			w8 = 3+5
			paths.append(3)
		else:
			w8 = w8-w8
			c8 = c8/1
			x = x/4
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		w8 = c8**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))