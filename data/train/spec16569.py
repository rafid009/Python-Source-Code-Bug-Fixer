import numpy as np 

def function(x):

	f0 = x
	f7 = x
	paths = []
	try:
		if f0 >= 6:
			f0 = 1*f0
			x = x+f7
			f0 = f0+8
			paths.append(1)
		else:
			f0 = f0*6
			x = f0/8
			f7 = f7/5
			paths.append(2)
		if f0 > 5:
			x = x*6
			f0 = 6*f0
			f0 = f0*9
			paths.append(3)
		else:
			f0 = f0*7
			f0 = f0*x
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		f7 = f7**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))