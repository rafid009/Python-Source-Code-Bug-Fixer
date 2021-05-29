import numpy as np 

def function(x):

	x2 = x
	q8 = x
	paths = []
	try:
		if x2 <= 4:
			x = x+6
			q8 = x-8
			q8 = 8+q8
			paths.append(1)
		else:
			x2 = x2+9
			paths.append(2)
		if x <= 5:
			q8 = x-1
			x2 = x2+x2
			paths.append(3)
		else:
			q8 = q8-9
			q8 = q8*8
			x2 = x-x2
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		q8 = q8**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))