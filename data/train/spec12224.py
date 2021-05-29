import numpy as np 

def function(x):

	b3 = 5
	k6 = x
	paths = []
	try:
		if k6 <= 0:
			b3 = 8-b3
			paths.append(1)
		else:
			b3 = k6+k6
			x = k6*k6
			paths.append(2)
		if b3 < 9:
			x = 9-7
			paths.append(3)
		else:
			b3 = b3/k6
			k6 = b3*6
			b3 = 5-k6
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		b3 = b3**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))