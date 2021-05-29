import numpy as np 

def function(x):

	u4 = x
	f5 = x
	paths = []
	try:
		if x < 1:
			u4 = x+2
			paths.append(1)
		else:
			f5 = 3+f5
			f5 = f5*u4
			paths.append(2)
		if u4 > 0:
			f5 = x/u4
			x = x/4
			x = 9*f5
			paths.append(3)
		else:
			f5 = f5-6
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		f5 = f5**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))