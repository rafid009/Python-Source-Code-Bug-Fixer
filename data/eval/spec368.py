import numpy as np 

def function(x):

	r7 = x
	f5 = 0
	paths = []
	try:
		if r7 > 4:
			x = x-7
			x = x+x
			f5 = f5/x
			paths.append(1)
		else:
			r7 = 6+r7
			r7 = 4/r7
			paths.append(2)
		if x < 8:
			x = r7-3
			paths.append(3)
		else:
			x = x+2
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