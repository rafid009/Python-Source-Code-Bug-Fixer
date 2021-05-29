import numpy as np 

def function(x):

	i5 = x
	x2 = x
	paths = []
	try:
		if i5 > 0:
			x = 4*x
			i5 = i5+4
			paths.append(1)
		else:
			x2 = 7-4
			paths.append(2)
		if x <= 1:
			i5 = x2-7
			i5 = i5/x2
			i5 = x-i5
			paths.append(3)
		else:
			x = 6-x
			x = x+x
			x2 = x2*5
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		i5 = i5**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))