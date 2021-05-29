import numpy as np 

def function(x):

	r1 = x
	a5 = 4
	paths = []
	try:
		if a5 <= 8:
			r1 = r1/a5
			a5 = x-2
			paths.append(1)
		else:
			a5 = 6+x
			x = x*7
			r1 = x/2
			paths.append(2)
		if r1 > 4:
			r1 = 5+r1
			paths.append(3)
		else:
			r1 = x+r1
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		r1 = r1**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))