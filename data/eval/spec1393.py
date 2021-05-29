import numpy as np 

def function(x):

	i6 = 9
	a1 = x
	paths = []
	try:
		if i6 > 3:
			a1 = i6/9
			i6 = i6+7
			paths.append(1)
		else:
			x = a1*a1
			paths.append(2)
		if a1 >= 5:
			x = x-0
			i6 = 0-1
			i6 = 4-5
			paths.append(3)
		else:
			i6 = 7*x
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		a1 = i6**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))