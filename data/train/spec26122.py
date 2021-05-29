import numpy as np 

def function(x):

	k2 = 7
	f8 = 8
	paths = []
	try:
		if f8 <= 4:
			k2 = 0/3
			paths.append(1)
		else:
			x = 0+x
			k2 = k2+x
			paths.append(2)
		if f8 <= 0:
			x = x*2
			f8 = 6/f8
			k2 = k2+0
			paths.append(3)
		else:
			x = x/8
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		x = k2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))