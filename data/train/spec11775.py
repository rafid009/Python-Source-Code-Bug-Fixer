import numpy as np 

def function(x):

	i2 = 9
	j7 = 8
	paths = []
	try:
		if j7 >= 6:
			i2 = j7*x
			i2 = 2-6
			paths.append(1)
		else:
			j7 = j7*9
			j7 = j7*9
			paths.append(2)
		if x < 7:
			x = x+2
			i2 = 4*x
			paths.append(3)
		else:
			i2 = 3+6
			i2 = 5*7
			x = i2/4
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		j7 = i2**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))