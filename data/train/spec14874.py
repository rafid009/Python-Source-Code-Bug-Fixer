import numpy as np 

def function(x):

	b3 = x
	r7 = 1
	paths = []
	try:
		if x > 7:
			x = 4/x
			paths.append(1)
		else:
			x = 5/b3
			x = 6*x
			r7 = r7+x
			paths.append(2)
		if b3 < 9:
			x = x*8
			paths.append(3)
		else:
			b3 = 3-b3
			x = 4/1
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