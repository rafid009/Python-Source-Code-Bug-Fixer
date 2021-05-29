import numpy as np 

def function(x):

	j5 = 4
	i9 = x
	paths = []
	try:
		if i9 >= 8:
			x = j5-x
			x = j5*2
			x = 0-x
			paths.append(1)
		else:
			x = x/7
			i9 = 1/i9
			paths.append(2)
		if j5 < 7:
			j5 = x*j5
			j5 = j5-1
			paths.append(3)
		else:
			i9 = x-j5
			x = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j5 = x**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))