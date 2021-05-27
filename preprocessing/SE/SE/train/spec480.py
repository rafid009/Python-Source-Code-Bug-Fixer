import numpy as np 

def function(x):

	v9 = 8
	b8 = x
	paths = []
	try:
		if b8 < 1:
			x = 0+x
			paths.append(1)
		else:
			x = 8-2
			x = b8-x
			b8 = b8-4
			paths.append(2)
		if b8 >= 4:
			v9 = b8-v9
			paths.append(3)
		else:
			x = b8/3
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		b8 = v9**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))