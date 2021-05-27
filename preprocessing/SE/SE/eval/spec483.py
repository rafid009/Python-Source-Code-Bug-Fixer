import numpy as np 

def function(x):

	i6 = 1
	r3 = 2
	paths = []
	try:
		if x <= 6:
			x = x+x
			paths.append(1)
		else:
			x = i6/9
			paths.append(2)
		if i6 <= 7:
			r3 = r3+7
			i6 = i6-7
			paths.append(3)
		else:
			i6 = i6/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))