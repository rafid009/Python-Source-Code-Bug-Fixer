import numpy as np 

def function(x):

	n4 = 3
	f0 = x
	paths = []
	try:
		if f0 >= 8:
			n4 = n4*1
			f0 = 2-f0
			n4 = 1/n4
			paths.append(1)
		else:
			x = n4*x
			n4 = n4/3
			paths.append(2)
		if x < 1:
			n4 = n4/n4
			paths.append(3)
		else:
			x = n4/f0
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