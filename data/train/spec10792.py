import numpy as np 

def function(x):

	e9 = 1
	r7 = x
	paths = []
	try:
		if e9 <= 5:
			e9 = 1+e9
			paths.append(1)
		else:
			r7 = 3+x
			x = 8+5
			x = 5-0
			paths.append(2)
		if r7 < 2:
			x = x-0
			paths.append(3)
		else:
			x = x/5
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		e9 = r7**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))