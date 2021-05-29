import numpy as np 

def function(x):

	r1 = x
	k7 = x
	paths = []
	try:
		if r1 <= 5:
			k7 = r1/6
			r1 = 8+r1
			paths.append(1)
		else:
			x = x+0
			r1 = r1/4
			paths.append(2)
		if r1 <= 5:
			k7 = k7*9
			r1 = r1/7
			r1 = r1-r1
			paths.append(3)
		else:
			x = x/1
			k7 = 5+0
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		r1 = k7**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))