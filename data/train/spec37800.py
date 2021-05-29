import numpy as np 

def function(x):

	j7 = 2
	i2 = x
	paths = []
	try:
		if j7 >= 8:
			x = 6*4
			paths.append(1)
		else:
			x = 3+i2
			x = 5/x
			i2 = i2-8
			paths.append(2)
		if x <= 7:
			i2 = i2*5
			j7 = 9/6
			i2 = 9-j7
			paths.append(3)
		else:
			j7 = 0/j7
			x = x*x
			j7 = j7-j7
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