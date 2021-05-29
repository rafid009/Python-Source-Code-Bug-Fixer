import numpy as np 

def function(x):

	r3 = 4
	y6 = x
	paths = []
	try:
		if r3 >= 3:
			r3 = y6+5
			x = 8*x
			x = x/2
			paths.append(1)
		else:
			r3 = r3+y6
			y6 = y6+x
			y6 = y6-7
			paths.append(2)
		if r3 < 6:
			x = 1*7
			y6 = 6-y6
			paths.append(3)
		else:
			x = 5-5
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		y6 = r3**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))