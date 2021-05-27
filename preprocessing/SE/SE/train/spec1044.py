import numpy as np 

def function(x):

	r6 = x
	a5 = 6
	x = x
	paths = []
	try:
		if r6 <= 7:
			x = a5+2
			paths.append(1)
		else:
			a5 = 1*4
			a5 = 4-a5
			a5 = a5*a5
			paths.append(2)
		if a5 >= 7:
			a5 = r6-a5
			r6 = r6*3
			x = x*a5
			paths.append(3)
		else:
			x = x-0
			x = x/7
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		a5 = r6**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))