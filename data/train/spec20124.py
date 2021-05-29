import numpy as np 

def function(x):

	e9 = 0
	v0 = 9
	x = x
	paths = []
	try:
		if x > 3:
			e9 = 8-e9
			x = x*7
			v0 = e9/x
			paths.append(1)
		else:
			e9 = x+0
			v0 = 4/x
			x = v0/x
			paths.append(2)
		if x > 9:
			x = 2-x
			v0 = 4/4
			x = 8/e9
			paths.append(3)
		else:
			v0 = v0*1
			v0 = v0/7
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		x = e9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))