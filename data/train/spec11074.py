import numpy as np 

def function(x):

	b9 = x
	q8 = 6
	paths = []
	try:
		if b9 >= 6:
			q8 = q8+4
			x = 7*1
			paths.append(1)
		else:
			q8 = q8/1
			q8 = q8-b9
			b9 = b9-5
			paths.append(2)
		if x < 3:
			b9 = b9-6
			b9 = x-q8
			paths.append(3)
		else:
			x = b9-x
			b9 = 6-2
			q8 = 4+x
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		b9 = q8**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))