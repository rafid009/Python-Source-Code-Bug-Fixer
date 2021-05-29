import numpy as np 

def function(x):

	v2 = 6
	k9 = x
	paths = []
	try:
		if v2 >= 3:
			k9 = 1+k9
			paths.append(1)
		else:
			k9 = k9-2
			x = x+x
			paths.append(2)
		if v2 < 1:
			x = x+1
			k9 = k9-x
			x = k9/x
			paths.append(3)
		else:
			x = 4/x
			v2 = k9+v2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v2 = x**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))