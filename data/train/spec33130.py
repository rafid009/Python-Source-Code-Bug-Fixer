import numpy as np 

def function(x):

	k7 = 9
	j5 = x
	paths = []
	try:
		if x < 2:
			k7 = x-7
			x = x-6
			x = x*7
			paths.append(1)
		else:
			k7 = 5/k7
			k7 = 4+j5
			paths.append(2)
		if k7 >= 1:
			j5 = 4*j5
			k7 = 6*1
			paths.append(3)
		else:
			k7 = k7+6
			j5 = x-j5
			x = x-4
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		j5 = k7**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))