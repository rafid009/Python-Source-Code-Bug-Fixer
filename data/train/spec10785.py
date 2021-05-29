import numpy as np 

def function(x):

	f0 = 2
	x0 = 2
	x = x
	paths = []
	try:
		if f0 < 3:
			x = x0+x
			x0 = f0+8
			paths.append(1)
		else:
			f0 = f0/x
			x0 = f0/x0
			x0 = 2+x0
			paths.append(2)
		if x <= 9:
			x0 = x0+5
			x = x-x
			x0 = 5/7
			paths.append(3)
		else:
			f0 = 6-9
			x0 = x0-8
			f0 = x/f0
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