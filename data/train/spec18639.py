import numpy as np 

def function(x):

	b5 = x
	i6 = x
	paths = []
	try:
		if b5 > 3:
			x = x-3
			i6 = 5+i6
			paths.append(1)
		else:
			i6 = 3+i6
			b5 = b5-6
			paths.append(2)
		if x > 4:
			b5 = i6-b5
			b5 = x/8
			i6 = 7*5
			paths.append(3)
		else:
			i6 = 1-2
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		i6 = b5**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))