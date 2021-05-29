import numpy as np 

def function(x):

	b5 = x
	j9 = 6
	paths = []
	try:
		if j9 < 7:
			b5 = 1+j9
			j9 = j9/6
			b5 = 9-b5
			paths.append(1)
		else:
			b5 = x+7
			b5 = 5-j9
			paths.append(2)
		if x >= 1:
			b5 = x/b5
			j9 = 7/b5
			j9 = j9+5
			paths.append(3)
		else:
			j9 = j9+x
			b5 = x/j9
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		x = b5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))