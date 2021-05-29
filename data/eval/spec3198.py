import numpy as np 

def function(x):

	j4 = x
	k2 = 8
	paths = []
	try:
		if j4 < 8:
			k2 = k2*k2
			k2 = k2-4
			paths.append(1)
		else:
			k2 = k2-j4
			j4 = j4*j4
			j4 = j4+x
			paths.append(2)
		if k2 > 5:
			j4 = 3-k2
			x = k2/x
			k2 = k2-x
			paths.append(3)
		else:
			j4 = 9+j4
			j4 = j4-0
			j4 = 0/j4
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