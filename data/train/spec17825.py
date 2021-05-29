import numpy as np 

def function(x):

	k6 = 3
	v2 = x
	paths = []
	try:
		if v2 < 9:
			k6 = v2+k6
			x = 2-x
			paths.append(1)
		else:
			k6 = k6+v2
			v2 = 0-k6
			v2 = v2-4
			paths.append(2)
		if v2 < 3:
			x = x/3
			k6 = k6*v2
			k6 = 4-k6
			paths.append(3)
		else:
			v2 = v2*3
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		k6 = k6**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))