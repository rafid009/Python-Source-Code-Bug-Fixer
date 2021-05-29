import numpy as np 

def function(x):

	f3 = 0
	u5 = x
	paths = []
	try:
		if f3 <= 0:
			x = 1-x
			paths.append(1)
		else:
			u5 = 6*7
			x = f3*1
			x = x*3
			paths.append(2)
		if u5 >= 6:
			f3 = f3+4
			x = x+0
			f3 = 0+f3
			paths.append(3)
		else:
			x = 7/x
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