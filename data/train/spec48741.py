import numpy as np 

def function(x):

	j5 = x
	k5 = 1
	paths = []
	try:
		if x <= 1:
			x = k5/9
			paths.append(1)
		else:
			j5 = x*5
			paths.append(2)
		if x < 4:
			k5 = 0-k5
			j5 = j5-2
			x = 9-j5
			paths.append(3)
		else:
			j5 = j5*x
			j5 = j5*0
			k5 = k5*3
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