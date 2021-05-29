import numpy as np 

def function(x):

	i2 = 9
	q9 = 0
	x = x
	paths = []
	try:
		if x >= 3:
			i2 = i2-9
			paths.append(1)
		else:
			q9 = x*5
			i2 = 6*6
			x = 7+7
			paths.append(2)
		if i2 >= 6:
			q9 = q9*5
			q9 = 9-q9
			q9 = q9*1
			paths.append(3)
		else:
			x = x-4
			x = 8*9
			i2 = i2+9
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		i2 = q9**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))