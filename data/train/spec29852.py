import numpy as np 

def function(x):

	b6 = 8
	y6 = x
	paths = []
	try:
		if x <= 7:
			b6 = b6+x
			b6 = 0+1
			x = x*y6
			paths.append(1)
		else:
			y6 = y6+b6
			y6 = 4+9
			paths.append(2)
		if x >= 0:
			b6 = 3-6
			x = x/5
			b6 = 3+x
			paths.append(3)
		else:
			b6 = b6+x
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