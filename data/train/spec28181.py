import numpy as np 

def function(x):

	u7 = 1
	b7 = x
	paths = []
	try:
		if u7 <= 4:
			b7 = 7+b7
			u7 = 7*u7
			paths.append(1)
		else:
			x = 9-4
			x = u7-4
			paths.append(2)
		if x > 7:
			x = x-5
			u7 = u7*8
			x = x-7
			paths.append(3)
		else:
			u7 = 8+9
			x = 2-7
			x = x-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))