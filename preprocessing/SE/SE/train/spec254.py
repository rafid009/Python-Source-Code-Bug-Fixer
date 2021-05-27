import numpy as np 

def function(x):

	i2 = 9
	a4 = 4
	x = x
	paths = []
	try:
		if i2 <= 0:
			a4 = i2-8
			a4 = a4/a4
			paths.append(1)
		else:
			x = x-i2
			i2 = 3*5
			i2 = x*3
			paths.append(2)
		if x >= 5:
			a4 = 7+a4
			a4 = 8/a4
			x = a4-x
			paths.append(3)
		else:
			x = x+a4
			a4 = 3+7
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		i2 = i2**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))