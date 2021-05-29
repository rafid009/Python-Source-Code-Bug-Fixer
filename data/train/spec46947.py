import numpy as np 

def function(x):

	x1 = x
	i4 = x
	paths = []
	try:
		if i4 <= 5:
			x1 = 3-0
			x = x+9
			paths.append(1)
		else:
			i4 = 3+i4
			x1 = 0/4
			x1 = x1*5
			paths.append(2)
		if i4 <= 8:
			x1 = x1*5
			i4 = x-x1
			x = x1*0
			paths.append(3)
		else:
			x1 = 0+x1
			i4 = 3/4
			i4 = 4+i4
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		x = i4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))