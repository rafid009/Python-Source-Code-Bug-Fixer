import numpy as np 

def function(x):

	f2 = 5
	k6 = x
	paths = []
	try:
		if f2 < 8:
			x = 1+x
			k6 = 0-k6
			f2 = f2+f2
			paths.append(1)
		else:
			k6 = 6+k6
			f2 = 3*f2
			f2 = k6-f2
			paths.append(2)
		if x < 5:
			x = 5+7
			f2 = 6-f2
			x = 7-x
			paths.append(3)
		else:
			x = 1/x
			f2 = f2-3
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		x = k6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))