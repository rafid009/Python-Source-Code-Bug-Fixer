import numpy as np 

def function(x):

	e7 = x
	x8 = 1
	x = x
	paths = []
	try:
		if e7 >= 7:
			e7 = e7/3
			x = x-9
			x8 = 6+x8
			paths.append(1)
		else:
			e7 = 0+e7
			paths.append(2)
		if e7 >= 2:
			e7 = 1*4
			x8 = 4/9
			x8 = x*0
			paths.append(3)
		else:
			x = 9+x
			e7 = x8-7
			x = e7*x8
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		x = e7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))