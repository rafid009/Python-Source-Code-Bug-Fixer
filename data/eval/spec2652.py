import numpy as np 

def function(x):

	j7 = 7
	n9 = 8
	paths = []
	try:
		if x <= 1:
			j7 = j7*6
			n9 = n9/1
			paths.append(1)
		else:
			x = x-x
			n9 = n9+7
			n9 = n9/8
			paths.append(2)
		if j7 < 4:
			n9 = x/4
			n9 = x-1
			n9 = 1*8
			paths.append(3)
		else:
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j7 = x**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))