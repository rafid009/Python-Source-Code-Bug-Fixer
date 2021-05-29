import numpy as np 

def function(x):

	r3 = 5
	a5 = 9
	paths = []
	try:
		if a5 > 4:
			a5 = a5-8
			a5 = 9-2
			a5 = r3+4
			paths.append(1)
		else:
			r3 = r3/a5
			r3 = x*5
			x = 3+x
			paths.append(2)
		if a5 <= 9:
			a5 = x*r3
			r3 = x/r3
			r3 = r3*5
			paths.append(3)
		else:
			r3 = r3/9
			x = x-8
			a5 = a5+0
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		x = r3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))