import numpy as np 

def function(x):

	e6 = 5
	r7 = 2
	paths = []
	try:
		if x >= 9:
			e6 = 1/e6
			x = x*8
			x = x+1
			paths.append(1)
		else:
			e6 = r7*6
			r7 = e6-9
			e6 = 9*2
			paths.append(2)
		if r7 > 9:
			e6 = r7+7
			paths.append(3)
		else:
			r7 = r7+x
			e6 = e6+5
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