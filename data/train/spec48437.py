import numpy as np 

def function(x):

	f5 = x
	u5 = 4
	paths = []
	try:
		if u5 <= 6:
			u5 = f5-u5
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if f5 < 8:
			u5 = f5-u5
			u5 = 3-u5
			paths.append(3)
		else:
			f5 = f5-9
			f5 = f5+4
			x = f5*5
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		u5 = u5**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))