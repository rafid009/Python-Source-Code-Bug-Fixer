import numpy as np 

def function(x):

	f9 = 6
	k6 = x
	paths = []
	try:
		if x <= 2:
			x = 8*f9
			x = x/k6
			paths.append(1)
		else:
			f9 = f9+7
			f9 = 9-f9
			k6 = k6+5
			paths.append(2)
		if x > 9:
			f9 = 2+k6
			paths.append(3)
		else:
			k6 = 6/k6
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