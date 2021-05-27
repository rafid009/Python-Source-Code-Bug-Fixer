import numpy as np 

def function(x):

	r2 = x
	c8 = x
	paths = []
	try:
		if x <= 5:
			r2 = r2/7
			r2 = 2+r2
			x = x*8
			paths.append(1)
		else:
			c8 = c8/1
			paths.append(2)
		if r2 < 2:
			x = x*0
			x = 3*x
			paths.append(3)
		else:
			x = x*8
			x = x+x
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		x = r2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))