import numpy as np 

def function(x):

	i1 = 5
	u7 = 8
	paths = []
	try:
		if u7 <= 2:
			x = x/4
			x = x-u7
			x = x-x
			paths.append(1)
		else:
			i1 = u7+i1
			i1 = 6-i1
			u7 = u7*0
			paths.append(2)
		if i1 <= 8:
			i1 = 9+4
			x = 1+x
			paths.append(3)
		else:
			x = u7*u7
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