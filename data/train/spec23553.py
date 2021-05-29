import numpy as np 

def function(x):

	f2 = x
	o9 = 1
	paths = []
	try:
		if x <= 0:
			x = 1-x
			o9 = o9+x
			paths.append(1)
		else:
			x = 2+5
			f2 = f2+1
			f2 = 3*1
			paths.append(2)
		if f2 > 9:
			f2 = f2+8
			paths.append(3)
		else:
			o9 = 7/o9
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