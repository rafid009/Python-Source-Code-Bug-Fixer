import numpy as np 

def function(x):

	v2 = 0
	f7 = 6
	x = 8
	paths = []
	try:
		if v2 <= 2:
			x = 0+f7
			v2 = v2-6
			x = x-4
			paths.append(1)
		else:
			v2 = 0/v2
			paths.append(2)
		if v2 < 9:
			f7 = v2-3
			v2 = v2*5
			x = 3*5
			paths.append(3)
		else:
			x = 8*v2
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		x = v2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))