import numpy as np 

def function(x):

	j3 = x
	i2 = x
	paths = []
	try:
		if x > 6:
			j3 = j3-x
			i2 = i2-9
			paths.append(1)
		else:
			x = 0/x
			j3 = j3-3
			paths.append(2)
		if i2 < 4:
			x = x*9
			paths.append(3)
		else:
			j3 = i2+3
			x = x+7
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