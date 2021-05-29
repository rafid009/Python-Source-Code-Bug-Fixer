import numpy as np 

def function(x):

	k1 = x
	j5 = x
	x = 7
	paths = []
	try:
		if j5 >= 6:
			j5 = 5/j5
			k1 = 8*k1
			k1 = k1/3
			paths.append(1)
		else:
			j5 = 8*j5
			x = 6+x
			paths.append(2)
		if x < 0:
			x = x-1
			k1 = k1+7
			k1 = 6+9
			paths.append(3)
		else:
			k1 = k1*j5
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		k1 = j5**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))