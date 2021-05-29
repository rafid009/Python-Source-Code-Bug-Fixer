import numpy as np 

def function(x):

	v2 = x
	k1 = x
	paths = []
	try:
		if v2 < 2:
			k1 = k1-k1
			k1 = x/3
			x = 9+x
			paths.append(1)
		else:
			k1 = k1-0
			v2 = v2-v2
			k1 = 9/2
			paths.append(2)
		if x >= 2:
			x = 0-0
			x = 6*8
			v2 = 3-6
			paths.append(3)
		else:
			k1 = v2+v2
			v2 = 5/v2
			k1 = 3+9
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		v2 = k1**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))