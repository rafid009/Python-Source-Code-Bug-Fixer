import numpy as np 

def function(x):

	y5 = x
	y6 = 0
	paths = []
	try:
		if y6 >= 3:
			x = y5/7
			y5 = x*2
			x = 4+x
			paths.append(1)
		else:
			y6 = 0*y5
			y6 = 7/9
			y6 = y6/1
			paths.append(2)
		if y5 > 8:
			x = 4+0
			paths.append(3)
		else:
			y5 = y5/6
			y6 = 3*x
			y5 = y5/2
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		y6 = y6**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))