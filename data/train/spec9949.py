import numpy as np 

def function(x):

	v4 = 7
	k7 = x
	paths = []
	try:
		if x > 1:
			k7 = k7-1
			paths.append(1)
		else:
			v4 = v4+v4
			v4 = x*k7
			x = x+k7
			paths.append(2)
		if v4 <= 1:
			k7 = 0/k7
			paths.append(3)
		else:
			k7 = k7+4
			k7 = v4/k7
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		k7 = k7**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))