import numpy as np 

def function(x):

	b8 = 8
	i9 = x
	x = x
	paths = []
	try:
		if x >= 4:
			i9 = 2-3
			i9 = i9*0
			paths.append(1)
		else:
			x = 1-x
			i9 = 4/i9
			paths.append(2)
		if i9 < 4:
			b8 = b8+6
			x = x/8
			paths.append(3)
		else:
			x = x-i9
			x = 2+x
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