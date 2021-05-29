import numpy as np 

def function(x):

	v6 = x
	v4 = x
	paths = []
	try:
		if x < 5:
			x = 7-0
			v6 = 5+v6
			v4 = 5*v4
			paths.append(1)
		else:
			v4 = x*9
			x = 5-x
			paths.append(2)
		if x > 3:
			v6 = v6-1
			v6 = v6*1
			x = 0+1
			paths.append(3)
		else:
			x = x-0
			v4 = v6/x
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		x = v4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))