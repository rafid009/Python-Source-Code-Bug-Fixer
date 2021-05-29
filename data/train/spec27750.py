import numpy as np 

def function(x):

	k6 = x
	i8 = 0
	paths = []
	try:
		if x < 5:
			i8 = 1/4
			i8 = i8/i8
			paths.append(1)
		else:
			k6 = 4/k6
			k6 = k6+k6
			paths.append(2)
		if k6 <= 4:
			k6 = 9+k6
			k6 = 4*k6
			x = x+4
			paths.append(3)
		else:
			i8 = 8+7
			i8 = i8-k6
			k6 = 6*2
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		i8 = k6**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))