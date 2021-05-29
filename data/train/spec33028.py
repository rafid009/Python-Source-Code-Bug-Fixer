import numpy as np 

def function(x):

	u3 = x
	e8 = x
	paths = []
	try:
		if e8 > 6:
			u3 = 4+u3
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if x >= 3:
			u3 = x/7
			paths.append(3)
		else:
			u3 = e8-3
			x = x*4
			u3 = 9/u3
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		u3 = e8**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))