import numpy as np 

def function(x):

	i9 = x
	u4 = 9
	paths = []
	try:
		if x > 5:
			i9 = 2+i9
			x = 2-x
			paths.append(1)
		else:
			x = x*x
			x = 8+x
			paths.append(2)
		if u4 < 7:
			u4 = 2/u4
			u4 = u4-7
			paths.append(3)
		else:
			i9 = 3+i9
			i9 = x-8
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		i9 = i9**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))