import numpy as np 

def function(x):

	f9 = x
	v6 = 2
	paths = []
	try:
		if v6 >= 4:
			f9 = x+4
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if f9 > 1:
			f9 = f9-1
			f9 = v6/f9
			x = x-8
			paths.append(3)
		else:
			f9 = f9+f9
			x = x/2
			v6 = v6-7
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		x = v6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))