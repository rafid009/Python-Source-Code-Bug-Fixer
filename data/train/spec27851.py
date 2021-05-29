import numpy as np 

def function(x):

	f5 = x
	f0 = 7
	paths = []
	try:
		if f5 < 0:
			x = x+3
			f0 = f0+4
			x = 1-x
			paths.append(1)
		else:
			f5 = 6/2
			f5 = x/f5
			f0 = f5-f0
			paths.append(2)
		if f0 <= 5:
			f0 = f0/5
			x = 7/1
			paths.append(3)
		else:
			f0 = 7*f0
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		f0 = f0**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))