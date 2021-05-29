import numpy as np 

def function(x):

	y4 = x
	y6 = x
	paths = []
	try:
		if x > 3:
			y6 = 4*x
			x = x+2
			x = x*2
			paths.append(1)
		else:
			y4 = y6*y6
			x = x+4
			y6 = 6+0
			paths.append(2)
		if x < 9:
			y4 = x/2
			y6 = y6*0
			paths.append(3)
		else:
			y4 = 8+y4
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		y4 = y4**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))