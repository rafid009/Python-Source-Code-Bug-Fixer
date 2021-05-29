import numpy as np 

def function(x):

	r9 = 5
	v6 = x
	x = 3
	paths = []
	try:
		if r9 >= 9:
			x = 3/x
			paths.append(1)
		else:
			r9 = x/v6
			x = x-0
			r9 = 4-9
			paths.append(2)
		if v6 > 2:
			x = 7+x
			r9 = 5+5
			r9 = r9/r9
			paths.append(3)
		else:
			x = r9+7
			r9 = r9*2
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		r9 = v6**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))