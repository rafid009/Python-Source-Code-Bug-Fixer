import numpy as np 

def function(x):

	r3 = x
	u7 = x
	paths = []
	try:
		if x <= 0:
			x = x-x
			u7 = 8*8
			u7 = x*r3
			paths.append(1)
		else:
			x = r3*7
			r3 = 8*r3
			u7 = u7/u7
			paths.append(2)
		if u7 <= 4:
			u7 = 2-0
			x = 9*x
			paths.append(3)
		else:
			u7 = 9-8
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		x = r3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))