import numpy as np 

def function(x):

	i2 = 0
	i6 = x
	paths = []
	try:
		if x <= 7:
			i6 = i6*2
			paths.append(1)
		else:
			i6 = 2-i6
			paths.append(2)
		if i6 <= 0:
			i6 = i6-4
			paths.append(3)
		else:
			i6 = i6-x
			i6 = x+i6
			i2 = 8*i2
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		x = i6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))