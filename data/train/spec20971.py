import numpy as np 

def function(x):

	e3 = x
	y3 = 3
	paths = []
	try:
		if x < 6:
			x = 0+5
			e3 = e3*1
			x = 0/x
			paths.append(1)
		else:
			x = e3-x
			x = x/y3
			y3 = e3+y3
			paths.append(2)
		if e3 <= 3:
			y3 = x/9
			paths.append(3)
		else:
			e3 = e3/e3
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		y3 = e3**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))