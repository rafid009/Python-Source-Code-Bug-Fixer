import numpy as np 

def function(x):

	k7 = x
	r6 = 2
	paths = []
	try:
		if r6 > 2:
			k7 = 7+k7
			k7 = k7+4
			paths.append(1)
		else:
			x = k7-x
			paths.append(2)
		if k7 <= 4:
			r6 = r6-8
			x = 4-1
			k7 = r6/5
			paths.append(3)
		else:
			k7 = k7-8
			k7 = 1+x
			r6 = r6-3
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		r6 = k7**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))