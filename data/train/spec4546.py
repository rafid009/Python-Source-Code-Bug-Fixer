import numpy as np 

def function(x):

	k6 = 2
	q4 = 7
	x = x
	paths = []
	try:
		if k6 >= 4:
			k6 = k6+0
			k6 = 2+5
			paths.append(1)
		else:
			x = x+8
			paths.append(2)
		if k6 <= 4:
			q4 = q4-1
			paths.append(3)
		else:
			x = 9/x
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