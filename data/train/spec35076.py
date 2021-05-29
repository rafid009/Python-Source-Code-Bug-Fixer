import numpy as np 

def function(x):

	f7 = 9
	i6 = 6
	paths = []
	try:
		if f7 > 0:
			i6 = 0*i6
			paths.append(1)
		else:
			f7 = 1/f7
			f7 = 6/3
			i6 = 0-i6
			paths.append(2)
		if x < 5:
			i6 = i6*6
			paths.append(3)
		else:
			i6 = i6-8
			f7 = 8+f7
			i6 = i6-9
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