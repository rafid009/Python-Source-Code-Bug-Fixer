import numpy as np 

def function(x):

	i9 = x
	f2 = 2
	paths = []
	try:
		if f2 >= 0:
			x = x+i9
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if x >= 7:
			x = x*6
			paths.append(3)
		else:
			x = x-i9
			f2 = 6/f2
			f2 = 6*i9
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		x = f2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))