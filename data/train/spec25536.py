import numpy as np 

def function(x):

	u3 = x
	q8 = x
	paths = []
	try:
		if x <= 0:
			q8 = 5-7
			paths.append(1)
		else:
			u3 = u3+x
			q8 = q8+1
			paths.append(2)
		if x < 4:
			u3 = u3/q8
			paths.append(3)
		else:
			u3 = 4+u3
			q8 = 8/1
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		x = q8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))