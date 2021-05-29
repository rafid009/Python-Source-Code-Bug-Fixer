import numpy as np 

def function(x):

	f2 = x
	c5 = 0
	paths = []
	try:
		if c5 < 4:
			f2 = 2+4
			x = 5*x
			f2 = f2+c5
			paths.append(1)
		else:
			c5 = c5/8
			c5 = 0*9
			paths.append(2)
		if x <= 3:
			f2 = x+f2
			f2 = f2*8
			x = x/2
			paths.append(3)
		else:
			c5 = c5+0
			f2 = f2+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f2 = x**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))