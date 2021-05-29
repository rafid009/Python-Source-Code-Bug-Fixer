import numpy as np 

def function(x):

	j5 = 6
	k7 = x
	paths = []
	try:
		if x < 3:
			k7 = 7+k7
			x = 3-j5
			x = x+7
			paths.append(1)
		else:
			k7 = j5*j5
			j5 = 3-j5
			k7 = 6-k7
			paths.append(2)
		if x <= 9:
			x = 3*k7
			j5 = j5*x
			x = x*3
			paths.append(3)
		else:
			j5 = 8*6
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		k7 = k7**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))