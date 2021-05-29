import numpy as np 

def function(x):

	f4 = 9
	i6 = 4
	paths = []
	try:
		if x < 3:
			i6 = 2*i6
			x = 0+x
			f4 = f4+7
			paths.append(1)
		else:
			f4 = x-0
			f4 = f4+1
			paths.append(2)
		if i6 <= 8:
			i6 = 6-7
			paths.append(3)
		else:
			f4 = 2-x
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