import numpy as np 

def function(x):

	u1 = 2
	i7 = x
	paths = []
	try:
		if u1 >= 2:
			x = x-4
			x = x+5
			paths.append(1)
		else:
			i7 = i7*8
			x = i7+x
			x = i7-x
			paths.append(2)
		if x >= 4:
			u1 = u1/8
			x = x*i7
			paths.append(3)
		else:
			u1 = 3/u1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))