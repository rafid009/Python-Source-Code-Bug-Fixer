import numpy as np 

def function(x):

	a7 = x
	j9 = 9
	paths = []
	try:
		if x <= 2:
			j9 = j9-2
			a7 = a7/2
			j9 = j9/1
			paths.append(1)
		else:
			x = x/8
			a7 = 6/j9
			x = 9+j9
			paths.append(2)
		if j9 <= 7:
			j9 = 2-j9
			j9 = j9*0
			paths.append(3)
		else:
			j9 = 1-j9
			x = x+8
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		x = a7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))