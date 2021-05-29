import numpy as np 

def function(x):

	r6 = 3
	y8 = 8
	paths = []
	try:
		if r6 <= 3:
			r6 = r6-x
			r6 = y8+r6
			paths.append(1)
		else:
			y8 = y8-1
			x = 1+r6
			paths.append(2)
		if x <= 0:
			x = x/4
			x = 5+0
			x = 5-x
			paths.append(3)
		else:
			y8 = 9+3
			x = x*7
			y8 = y8*6
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		x = r6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))