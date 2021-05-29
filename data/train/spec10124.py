import numpy as np 

def function(x):

	k6 = x
	f1 = x
	paths = []
	try:
		if k6 <= 3:
			x = 7-1
			paths.append(1)
		else:
			k6 = 3-k6
			paths.append(2)
		if k6 <= 2:
			k6 = k6/3
			x = f1*x
			paths.append(3)
		else:
			k6 = 4+8
			x = x/1
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		f1 = k6**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))