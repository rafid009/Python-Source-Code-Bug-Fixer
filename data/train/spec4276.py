import numpy as np 

def function(x):

	q8 = x
	i9 = 2
	paths = []
	try:
		if q8 > 8:
			q8 = 0+4
			paths.append(1)
		else:
			q8 = x+q8
			paths.append(2)
		if q8 >= 0:
			x = x*q8
			i9 = 3-5
			q8 = q8*0
			paths.append(3)
		else:
			x = x/6
			i9 = i9/4
			q8 = 7*7
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		i9 = i9**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))