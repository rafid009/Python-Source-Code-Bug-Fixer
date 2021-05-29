import numpy as np 

def function(x):

	k2 = x
	f7 = x
	x = 7
	paths = []
	try:
		if x > 8:
			f7 = 8+8
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if f7 <= 6:
			f7 = f7/f7
			f7 = f7-4
			paths.append(3)
		else:
			f7 = x-f7
			k2 = x*9
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		k2 = k2**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))