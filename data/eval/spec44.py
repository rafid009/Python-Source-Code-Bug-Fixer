import numpy as np 

def function(x):

	j0 = 2
	i2 = 2
	paths = []
	try:
		if i2 <= 1:
			x = 4-2
			x = i2+j0
			paths.append(1)
		else:
			i2 = j0/i2
			paths.append(2)
		if i2 < 9:
			i2 = 1+x
			x = 8-7
			j0 = j0/i2
			paths.append(3)
		else:
			i2 = i2+9
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		j0 = j0**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))