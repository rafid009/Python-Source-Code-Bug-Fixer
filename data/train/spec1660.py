import numpy as np 

def function(x):

	x7 = x
	f0 = x
	paths = []
	try:
		if x <= 5:
			x7 = x7*x7
			x = x-1
			paths.append(1)
		else:
			x7 = 1*x7
			paths.append(2)
		if f0 <= 8:
			x7 = 6-6
			x = x*1
			x = x7*1
			paths.append(3)
		else:
			x = x/4
			x = 0*x
			x = x/1
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		x = f0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))