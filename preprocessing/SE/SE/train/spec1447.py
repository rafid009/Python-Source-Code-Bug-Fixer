import numpy as np 

def function(x):

	k1 = 4
	r7 = 0
	paths = []
	try:
		if x <= 0:
			r7 = 8+5
			paths.append(1)
		else:
			x = 0/x
			r7 = 1-r7
			x = x+x
			paths.append(2)
		if r7 <= 5:
			k1 = r7-k1
			x = x+k1
			x = 7*8
			paths.append(3)
		else:
			k1 = r7+r7
			x = x/8
			r7 = 3-8
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