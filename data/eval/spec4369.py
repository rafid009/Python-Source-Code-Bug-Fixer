import numpy as np 

def function(x):

	f3 = 6
	y5 = 3
	paths = []
	try:
		if x >= 5:
			f3 = f3-5
			y5 = f3-6
			f3 = 1*9
			paths.append(1)
		else:
			x = 3+x
			y5 = y5*4
			paths.append(2)
		if f3 < 4:
			f3 = 8+y5
			y5 = y5/3
			y5 = f3/5
			paths.append(3)
		else:
			f3 = 8+f3
			f3 = 7+f3
			x = x+f3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y5 = x**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))