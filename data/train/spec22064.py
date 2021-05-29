import numpy as np 

def function(x):

	k6 = 5
	i6 = x
	paths = []
	try:
		if k6 < 6:
			i6 = i6+i6
			x = x-x
			paths.append(1)
		else:
			k6 = 9-3
			paths.append(2)
		if k6 <= 0:
			i6 = i6/k6
			i6 = i6+7
			x = 6-x
			paths.append(3)
		else:
			i6 = x-5
			k6 = x-3
			i6 = k6/i6
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