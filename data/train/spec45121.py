import numpy as np 

def function(x):

	x6 = x
	u3 = 1
	paths = []
	try:
		if u3 < 1:
			u3 = 5-u3
			x6 = 5-3
			paths.append(1)
		else:
			u3 = x-4
			u3 = u3+u3
			x = 3+0
			paths.append(2)
		if x > 9:
			u3 = u3/6
			x6 = 3/7
			x6 = 0+u3
			paths.append(3)
		else:
			x6 = x6/x
			x = x/4
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