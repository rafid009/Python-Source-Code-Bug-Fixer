import numpy as np 

def function(x):

	k7 = x
	j6 = 6
	paths = []
	try:
		if j6 > 9:
			j6 = j6+7
			x = x/x
			j6 = 0+1
			paths.append(1)
		else:
			k7 = k7/x
			paths.append(2)
		if k7 >= 9:
			k7 = 4+6
			x = x*7
			paths.append(3)
		else:
			k7 = k7*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))