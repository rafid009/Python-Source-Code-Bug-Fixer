import numpy as np 

def function(x):

	v3 = x
	k7 = x
	x = 5
	paths = []
	try:
		if x >= 0:
			x = k7+x
			k7 = k7+k7
			k7 = k7/1
			paths.append(1)
		else:
			k7 = k7*v3
			paths.append(2)
		if x >= 2:
			k7 = 0+k7
			v3 = v3+3
			paths.append(3)
		else:
			x = v3+1
			k7 = 0*v3
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		x = v3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))