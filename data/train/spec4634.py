import numpy as np 

def function(x):

	i4 = 6
	i5 = 2
	paths = []
	try:
		if i4 <= 7:
			i4 = 9*i4
			i5 = 7/i5
			paths.append(1)
		else:
			i4 = 0-i4
			i4 = i4*i4
			paths.append(2)
		if i4 < 3:
			i4 = 5*i4
			x = x+x
			i5 = 3+1
			paths.append(3)
		else:
			i5 = 0/i5
			i4 = i4+i4
			i5 = i5+2
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