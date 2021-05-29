import numpy as np 

def function(x):

	r9 = x
	u9 = 0
	paths = []
	try:
		if x >= 9:
			r9 = 0*r9
			r9 = r9*8
			r9 = 9+x
			paths.append(1)
		else:
			r9 = r9/3
			u9 = x+u9
			paths.append(2)
		if x >= 4:
			u9 = u9-x
			r9 = x+0
			paths.append(3)
		else:
			r9 = r9*2
			u9 = 0-0
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		r9 = r9**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))