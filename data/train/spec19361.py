import numpy as np 

def function(x):

	u5 = 3
	d6 = x
	paths = []
	try:
		if u5 < 0:
			x = 7/x
			paths.append(1)
		else:
			u5 = u5/4
			d6 = 4-d6
			u5 = u5-u5
			paths.append(2)
		if u5 <= 6:
			u5 = u5*3
			paths.append(3)
		else:
			x = 0+4
			x = x+d6
			d6 = 8/d6
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		u5 = d6**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))