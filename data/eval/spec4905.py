import numpy as np 

def function(x):

	x1 = 4
	r5 = x
	x = x
	paths = []
	try:
		if x <= 1:
			r5 = x1/r5
			paths.append(1)
		else:
			r5 = r5/x1
			paths.append(2)
		if x1 >= 8:
			x1 = 5-x1
			r5 = 9*7
			x = 1+x
			paths.append(3)
		else:
			x = x+8
			x = 4/7
			x1 = 7*2
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		x = r5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))