import numpy as np 

def function(x):

	y2 = 5
	i2 = x
	paths = []
	try:
		if y2 > 2:
			i2 = 9-i2
			x = i2+x
			paths.append(1)
		else:
			x = 1+i2
			paths.append(2)
		if i2 <= 8:
			y2 = y2/1
			y2 = y2-4
			y2 = y2/7
			paths.append(3)
		else:
			i2 = 4*2
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