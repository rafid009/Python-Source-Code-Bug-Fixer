import numpy as np 

def function(x):

	f5 = x
	f0 = 4
	paths = []
	try:
		if f0 >= 4:
			x = x/1
			x = 3-7
			f0 = f0-0
			paths.append(1)
		else:
			f0 = f0+f0
			x = x-8
			paths.append(2)
		if x > 0:
			x = 8*x
			f5 = f5+1
			x = 3-4
			paths.append(3)
		else:
			x = x-2
			f0 = f0/1
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		f0 = f5**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))