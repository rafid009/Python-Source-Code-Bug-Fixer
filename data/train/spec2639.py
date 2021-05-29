import numpy as np 

def function(x):

	x6 = 5
	i6 = 4
	paths = []
	try:
		if x6 <= 9:
			x6 = 1*2
			x6 = 0/x6
			x6 = x6/x
			paths.append(1)
		else:
			i6 = x*i6
			x = 7*x
			i6 = x6-3
			paths.append(2)
		if i6 <= 7:
			x6 = x6/1
			i6 = 0-3
			paths.append(3)
		else:
			i6 = i6-x6
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