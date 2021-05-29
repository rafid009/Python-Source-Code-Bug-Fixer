import numpy as np 

def function(x):

	c0 = 9
	e2 = 4
	x = x
	paths = []
	try:
		if x <= 7:
			x = 8*2
			paths.append(1)
		else:
			c0 = 0+3
			x = 9+c0
			x = x*0
			paths.append(2)
		if x > 0:
			e2 = e2-c0
			e2 = x/e2
			paths.append(3)
		else:
			c0 = 5-7
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		e2 = c0**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))