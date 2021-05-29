import numpy as np 

def function(x):

	k1 = x
	j5 = 6
	paths = []
	try:
		if x >= 6:
			k1 = 3/1
			paths.append(1)
		else:
			x = x-6
			x = x*4
			j5 = k1*k1
			paths.append(2)
		if j5 <= 9:
			j5 = j5*6
			paths.append(3)
		else:
			x = 2-x
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		j5 = k1**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))