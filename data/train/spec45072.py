import numpy as np 

def function(x):

	v3 = 5
	b9 = x
	paths = []
	try:
		if x >= 6:
			x = 0-x
			paths.append(1)
		else:
			v3 = 7/v3
			b9 = v3+b9
			paths.append(2)
		if v3 > 2:
			v3 = 0+x
			paths.append(3)
		else:
			b9 = b9/1
			v3 = v3/v3
			x = x-v3
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		b9 = v3**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))