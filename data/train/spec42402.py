import numpy as np 

def function(x):

	k2 = 0
	f2 = x
	paths = []
	try:
		if k2 > 0:
			k2 = k2*4
			f2 = f2/4
			paths.append(1)
		else:
			k2 = x+2
			x = x*f2
			x = 9*x
			paths.append(2)
		if f2 > 8:
			k2 = 1-k2
			k2 = 1*5
			f2 = 6/f2
			paths.append(3)
		else:
			f2 = f2+9
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		k2 = f2**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))