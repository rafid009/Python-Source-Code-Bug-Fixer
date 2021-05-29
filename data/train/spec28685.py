import numpy as np 

def function(x):

	r5 = x
	k6 = x
	paths = []
	try:
		if x <= 7:
			x = x/9
			paths.append(1)
		else:
			x = x+8
			x = 9+x
			x = 0-8
			paths.append(2)
		if r5 < 8:
			x = x*8
			x = k6/r5
			r5 = r5-5
			paths.append(3)
		else:
			r5 = x/r5
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		k6 = r5**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))