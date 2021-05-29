import numpy as np 

def function(x):

	x6 = 7
	r7 = x
	paths = []
	try:
		if r7 < 7:
			x6 = x6+0
			paths.append(1)
		else:
			x6 = x6-9
			x6 = x6*8
			paths.append(2)
		if x6 <= 6:
			r7 = r7-7
			paths.append(3)
		else:
			x6 = x6/5
			x = x*x
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		x = r7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))