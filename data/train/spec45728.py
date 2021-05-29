import numpy as np 

def function(x):

	k1 = 4
	r9 = 2
	paths = []
	try:
		if r9 < 7:
			r9 = r9-0
			k1 = r9-3
			paths.append(1)
		else:
			k1 = k1/x
			paths.append(2)
		if k1 <= 9:
			x = x+1
			k1 = x*9
			r9 = r9/7
			paths.append(3)
		else:
			r9 = r9/5
			r9 = k1*4
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		r9 = k1**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))