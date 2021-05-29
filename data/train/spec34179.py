import numpy as np 

def function(x):

	r7 = 8
	u2 = 3
	paths = []
	try:
		if x > 5:
			r7 = r7*5
			r7 = 2-r7
			r7 = r7*3
			paths.append(1)
		else:
			x = u2+u2
			paths.append(2)
		if x < 7:
			u2 = 8+u2
			paths.append(3)
		else:
			u2 = 5+9
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		x = r7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))