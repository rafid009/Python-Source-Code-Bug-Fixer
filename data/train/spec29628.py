import numpy as np 

def function(x):

	u7 = 2
	f0 = 9
	paths = []
	try:
		if x <= 5:
			x = 7/x
			paths.append(1)
		else:
			x = x*x
			f0 = f0/3
			f0 = 7/f0
			paths.append(2)
		if x <= 7:
			u7 = u7+3
			x = 1/x
			f0 = f0+x
			paths.append(3)
		else:
			u7 = 1-u7
			u7 = u7*x
			u7 = f0*9
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		u7 = f0**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))