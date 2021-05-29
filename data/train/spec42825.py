import numpy as np 

def function(x):

	q9 = x
	h2 = x
	paths = []
	try:
		if x <= 5:
			x = x+4
			h2 = q9+q9
			paths.append(1)
		else:
			x = 7/x
			paths.append(2)
		if q9 <= 4:
			x = h2+x
			paths.append(3)
		else:
			x = 4-5
			h2 = x/3
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		q9 = h2**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))