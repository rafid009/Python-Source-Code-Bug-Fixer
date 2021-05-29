import numpy as np 

def function(x):

	e9 = 6
	u4 = 9
	paths = []
	try:
		if e9 <= 3:
			u4 = x+3
			x = 1/x
			paths.append(1)
		else:
			e9 = u4/e9
			paths.append(2)
		if u4 >= 0:
			e9 = e9+x
			paths.append(3)
		else:
			x = 4+4
			x = x+0
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		e9 = e9**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))