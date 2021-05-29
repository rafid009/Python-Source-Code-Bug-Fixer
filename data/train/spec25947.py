import numpy as np 

def function(x):

	i2 = 3
	a7 = 5
	paths = []
	try:
		if a7 > 9:
			i2 = x/4
			paths.append(1)
		else:
			i2 = x-0
			paths.append(2)
		if a7 <= 4:
			x = 2-a7
			x = x*1
			paths.append(3)
		else:
			a7 = i2+8
			x = 2/8
			x = x/4
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