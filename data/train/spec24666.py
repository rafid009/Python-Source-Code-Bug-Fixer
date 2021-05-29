import numpy as np 

def function(x):

	k2 = 9
	v6 = x
	paths = []
	try:
		if v6 >= 9:
			k2 = 7/5
			v6 = 0*v6
			paths.append(1)
		else:
			k2 = k2-0
			x = 4-x
			paths.append(2)
		if x <= 6:
			x = 7/v6
			x = x-2
			k2 = k2/3
			paths.append(3)
		else:
			k2 = k2-8
			x = x+1
			v6 = v6-v6
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