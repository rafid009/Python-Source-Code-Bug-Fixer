import numpy as np 

def function(x):

	k4 = 4
	b6 = 1
	paths = []
	try:
		if b6 >= 7:
			k4 = k4+x
			paths.append(1)
		else:
			x = x-8
			k4 = k4/9
			b6 = b6+x
			paths.append(2)
		if k4 > 9:
			x = 6*8
			x = k4+3
			x = x/8
			paths.append(3)
		else:
			b6 = b6/5
			k4 = 5-k4
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		k4 = b6**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))