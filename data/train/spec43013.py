import numpy as np 

def function(x):

	k6 = x
	b9 = x
	paths = []
	try:
		if x <= 1:
			k6 = k6-1
			b9 = k6*0
			paths.append(1)
		else:
			k6 = k6-9
			paths.append(2)
		if k6 >= 2:
			b9 = b9+b9
			x = 2-x
			paths.append(3)
		else:
			b9 = 8/x
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		b9 = k6**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))