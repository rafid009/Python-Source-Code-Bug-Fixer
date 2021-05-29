import numpy as np 

def function(x):

	y5 = 3
	e3 = x
	paths = []
	try:
		if e3 <= 1:
			y5 = x/1
			x = x+x
			y5 = x+y5
			paths.append(1)
		else:
			x = y5-x
			x = y5/3
			y5 = 1+y5
			paths.append(2)
		if x <= 5:
			x = x/6
			x = 3+5
			paths.append(3)
		else:
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		x = e3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))