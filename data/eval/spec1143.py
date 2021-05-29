import numpy as np 

def function(x):

	k2 = 9
	f3 = x
	paths = []
	try:
		if k2 >= 8:
			x = k2-x
			x = 1/x
			paths.append(1)
		else:
			k2 = k2*8
			paths.append(2)
		if k2 > 4:
			f3 = f3*x
			f3 = f3-8
			k2 = x+k2
			paths.append(3)
		else:
			x = x+6
			x = x*x
			x = 9+0
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		k2 = f3**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))