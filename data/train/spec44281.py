import numpy as np 

def function(x):

	j6 = x
	b5 = 1
	paths = []
	try:
		if x > 9:
			j6 = 4+j6
			paths.append(1)
		else:
			j6 = 7*4
			paths.append(2)
		if x <= 0:
			x = 2+x
			paths.append(3)
		else:
			x = x-9
			j6 = j6+7
			j6 = 3+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))