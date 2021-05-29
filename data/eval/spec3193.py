import numpy as np 

def function(x):

	y6 = x
	a4 = 9
	paths = []
	try:
		if a4 <= 8:
			x = x*0
			y6 = 9+a4
			paths.append(1)
		else:
			x = x+a4
			paths.append(2)
		if a4 <= 3:
			y6 = y6-8
			y6 = y6*7
			paths.append(3)
		else:
			a4 = a4-5
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		a4 = y6**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))