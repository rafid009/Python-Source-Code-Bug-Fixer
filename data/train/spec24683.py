import numpy as np 

def function(x):

	f4 = x
	f0 = 1
	paths = []
	try:
		if f0 <= 8:
			f0 = 5/f4
			x = 6*x
			f4 = f4+1
			paths.append(1)
		else:
			x = 5+x
			f0 = f4+0
			paths.append(2)
		if f0 <= 5:
			f0 = 5+f0
			f0 = 9-x
			paths.append(3)
		else:
			f0 = f0*6
			x = 1-9
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		f4 = f0**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))