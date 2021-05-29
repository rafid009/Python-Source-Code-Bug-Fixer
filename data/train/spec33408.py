import numpy as np 

def function(x):

	f2 = x
	f9 = x
	paths = []
	try:
		if f9 > 1:
			f2 = f2/9
			f2 = f2-f2
			paths.append(1)
		else:
			f2 = f2*7
			paths.append(2)
		if f2 < 5:
			x = x-f9
			f2 = f2+0
			paths.append(3)
		else:
			f2 = f2-f2
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