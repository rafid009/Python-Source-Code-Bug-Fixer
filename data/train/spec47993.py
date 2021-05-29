import numpy as np 

def function(x):

	r7 = x
	b5 = 9
	paths = []
	try:
		if r7 > 6:
			r7 = r7/b5
			b5 = 3-6
			paths.append(1)
		else:
			x = 1/x
			x = r7-x
			r7 = r7-7
			paths.append(2)
		if b5 <= 0:
			r7 = x-r7
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		b5 = r7**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))