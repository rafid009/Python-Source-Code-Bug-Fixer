import numpy as np 

def function(x):

	j6 = x
	k5 = x
	x = 5
	paths = []
	try:
		if j6 < 1:
			j6 = k5/3
			k5 = k5/8
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if k5 > 3:
			k5 = x/k5
			k5 = 9*k5
			x = 5-1
			paths.append(3)
		else:
			j6 = j6+6
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		j6 = k5**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))