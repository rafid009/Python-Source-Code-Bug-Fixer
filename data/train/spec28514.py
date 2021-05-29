import numpy as np 

def function(x):

	e9 = x
	x0 = 6
	paths = []
	try:
		if x0 <= 7:
			x0 = 1-x0
			x = 1*1
			paths.append(1)
		else:
			x0 = 4/7
			x0 = x0+9
			x = x+0
			paths.append(2)
		if x >= 4:
			x0 = x0*6
			e9 = 7/3
			x0 = 1+x0
			paths.append(3)
		else:
			e9 = e9/2
			x0 = 5/x
			x0 = x0+9
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		x0 = e9**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))