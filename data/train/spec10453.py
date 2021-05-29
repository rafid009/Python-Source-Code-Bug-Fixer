import numpy as np 

def function(x):

	q9 = 4
	v0 = x
	paths = []
	try:
		if x < 3:
			x = 6+x
			x = 7/v0
			paths.append(1)
		else:
			q9 = q9/3
			paths.append(2)
		if x < 9:
			q9 = q9/6
			v0 = 5-v0
			paths.append(3)
		else:
			q9 = q9+0
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		x = v0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))