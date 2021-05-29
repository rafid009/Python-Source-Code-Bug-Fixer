import numpy as np 

def function(x):

	e1 = 7
	k6 = 8
	x = x
	paths = []
	try:
		if x >= 2:
			k6 = 7/8
			x = k6*8
			paths.append(1)
		else:
			e1 = e1/8
			k6 = k6*0
			e1 = 7-e1
			paths.append(2)
		if x <= 9:
			k6 = k6-x
			e1 = e1-8
			x = 4-x
			paths.append(3)
		else:
			k6 = k6/k6
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