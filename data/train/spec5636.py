import numpy as np 

def function(x):

	d2 = 3
	u5 = x
	paths = []
	try:
		if d2 > 7:
			x = 7*2
			paths.append(1)
		else:
			u5 = u5+4
			x = 8+d2
			paths.append(2)
		if u5 <= 8:
			x = 7-x
			u5 = u5/6
			paths.append(3)
		else:
			u5 = u5-9
			x = x/2
			u5 = x+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u5 = x**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))