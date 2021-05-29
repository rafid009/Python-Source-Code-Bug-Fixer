import numpy as np 

def function(x):

	u1 = x
	y4 = x
	paths = []
	try:
		if u1 > 1:
			y4 = 7+9
			paths.append(1)
		else:
			y4 = 5*y4
			y4 = y4*0
			paths.append(2)
		if y4 >= 4:
			x = 6/x
			y4 = y4*u1
			paths.append(3)
		else:
			x = 1*x
			y4 = 0*y4
			x = x+x
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