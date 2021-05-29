import numpy as np 

def function(x):

	f6 = x
	f0 = 4
	x = x
	paths = []
	try:
		if f0 >= 2:
			x = x/9
			x = 7+x
			paths.append(1)
		else:
			x = f0+4
			paths.append(2)
		if f0 >= 9:
			x = f0-3
			x = x+x
			f0 = f0*f6
			paths.append(3)
		else:
			f6 = f6+3
			x = x/1
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		f0 = f6**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))