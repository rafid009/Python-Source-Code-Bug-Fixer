import numpy as np 

def function(x):

	r7 = x
	k7 = x
	paths = []
	try:
		if x >= 8:
			x = 2*x
			k7 = k7+x
			paths.append(1)
		else:
			k7 = k7-k7
			r7 = r7-x
			paths.append(2)
		if r7 > 5:
			r7 = 0-r7
			x = x*0
			paths.append(3)
		else:
			k7 = r7*8
			k7 = r7*0
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