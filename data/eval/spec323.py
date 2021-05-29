import numpy as np 

def function(x):

	k5 = 9
	i5 = x
	paths = []
	try:
		if x < 6:
			i5 = 3-i5
			paths.append(1)
		else:
			i5 = 4/7
			paths.append(2)
		if i5 < 3:
			x = 2-3
			x = k5/4
			paths.append(3)
		else:
			i5 = 4/i5
			k5 = x+k5
			k5 = x/k5
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		k5 = i5**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))