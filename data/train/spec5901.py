import numpy as np 

def function(x):

	k6 = x
	o3 = 4
	paths = []
	try:
		if o3 < 7:
			o3 = o3/2
			paths.append(1)
		else:
			k6 = k6+o3
			o3 = o3/7
			k6 = o3*o3
			paths.append(2)
		if x >= 4:
			o3 = 8+o3
			k6 = 9-k6
			k6 = 3+k6
			paths.append(3)
		else:
			k6 = 4*k6
			k6 = 5*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k6 = x**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))