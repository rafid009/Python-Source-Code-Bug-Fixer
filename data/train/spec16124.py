import numpy as np 

def function(x):

	r7 = x
	b8 = 8
	paths = []
	try:
		if x >= 5:
			b8 = x/r7
			r7 = r7+1
			paths.append(1)
		else:
			x = x*r7
			x = 3+1
			b8 = b8+0
			paths.append(2)
		if x > 5:
			b8 = 0/b8
			r7 = r7-4
			paths.append(3)
		else:
			x = x-r7
			x = 0/6
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		r7 = r7**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))