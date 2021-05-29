import numpy as np 

def function(x):

	y5 = 5
	d7 = x
	paths = []
	try:
		if d7 < 6:
			x = x/d7
			y5 = y5-5
			x = x/x
			paths.append(1)
		else:
			d7 = 4/7
			d7 = y5+x
			paths.append(2)
		if x > 1:
			y5 = 5*1
			y5 = y5-4
			y5 = y5+d7
			paths.append(3)
		else:
			y5 = d7+y5
			y5 = x*6
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		y5 = d7**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))