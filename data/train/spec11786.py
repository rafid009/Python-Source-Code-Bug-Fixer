import numpy as np 

def function(x):

	r7 = x
	l9 = x
	paths = []
	try:
		if l9 < 3:
			x = x+8
			paths.append(1)
		else:
			x = x*8
			paths.append(2)
		if x > 5:
			r7 = r7+l9
			l9 = r7-2
			paths.append(3)
		else:
			x = l9+3
			r7 = r7+x
			x = x-x
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