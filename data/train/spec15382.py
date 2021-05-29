import numpy as np 

def function(x):

	r2 = 3
	i1 = x
	paths = []
	try:
		if r2 <= 8:
			x = 9/x
			r2 = x+7
			paths.append(1)
		else:
			i1 = i1-6
			paths.append(2)
		if i1 <= 8:
			x = x*6
			r2 = r2+2
			x = 6+x
			paths.append(3)
		else:
			i1 = 2/i1
			x = x/8
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		i1 = r2**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))