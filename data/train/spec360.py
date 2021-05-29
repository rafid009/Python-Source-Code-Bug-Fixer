import numpy as np 

def function(x):

	i7 = x
	r1 = x
	paths = []
	try:
		if x <= 6:
			r1 = 4+i7
			i7 = 2/i7
			paths.append(1)
		else:
			i7 = 9/i7
			r1 = x+5
			i7 = r1+2
			paths.append(2)
		if r1 > 1:
			x = 9+x
			i7 = i7+x
			paths.append(3)
		else:
			r1 = r1-6
			r1 = x+r1
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		r1 = i7**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))