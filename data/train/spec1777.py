import numpy as np 

def function(x):

	k6 = 9
	x6 = x
	paths = []
	try:
		if x6 < 9:
			x6 = x6+1
			x6 = x+7
			x = x6/x
			paths.append(1)
		else:
			x = x/k6
			x6 = 3-7
			x6 = k6/x
			paths.append(2)
		if k6 < 7:
			x6 = k6+x6
			paths.append(3)
		else:
			k6 = k6*3
			k6 = k6-9
			k6 = 5+k6
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x6 = x6**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))