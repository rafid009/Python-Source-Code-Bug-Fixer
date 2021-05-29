import numpy as np 

def function(x):

	r7 = 2
	e6 = x
	paths = []
	try:
		if r7 > 4:
			e6 = e6*e6
			r7 = 8+r7
			x = x-4
			paths.append(1)
		else:
			x = 0+x
			e6 = 9/e6
			e6 = 0-e6
			paths.append(2)
		if x < 2:
			x = x*x
			e6 = 0*0
			paths.append(3)
		else:
			r7 = 0+r7
			r7 = e6*5
			e6 = e6-1
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