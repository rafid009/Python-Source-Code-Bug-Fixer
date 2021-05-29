import numpy as np 

def function(x):

	i5 = 6
	j0 = 4
	paths = []
	try:
		if x <= 5:
			j0 = j0-5
			paths.append(1)
		else:
			x = x*x
			j0 = i5+7
			paths.append(2)
		if i5 > 3:
			j0 = j0/9
			i5 = 3-i5
			x = 8-x
			paths.append(3)
		else:
			j0 = 4+j0
			i5 = i5*1
			i5 = i5/i5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))