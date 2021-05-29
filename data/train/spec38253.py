import numpy as np 

def function(x):

	a5 = 6
	i4 = 4
	paths = []
	try:
		if i4 > 2:
			a5 = 4+3
			paths.append(1)
		else:
			a5 = 1*a5
			a5 = a5+i4
			paths.append(2)
		if a5 <= 1:
			i4 = i4/1
			x = x+i4
			paths.append(3)
		else:
			a5 = x+a5
			a5 = 8-a5
			x = x-6
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		a5 = a5**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))