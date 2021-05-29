import numpy as np 

def function(x):

	r7 = 9
	u7 = 1
	x = x
	paths = []
	try:
		if u7 <= 4:
			x = x-2
			x = x-0
			paths.append(1)
		else:
			x = 4-x
			paths.append(2)
		if x > 2:
			x = r7*7
			r7 = 7+r7
			paths.append(3)
		else:
			u7 = x*u7
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		r7 = u7**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))