import numpy as np 

def function(x):

	r5 = 6
	q3 = 2
	paths = []
	try:
		if q3 <= 8:
			r5 = 5*7
			paths.append(1)
		else:
			q3 = 2+r5
			x = x*3
			paths.append(2)
		if r5 > 3:
			r5 = 2-r5
			x = x/6
			paths.append(3)
		else:
			q3 = 4/x
			x = 7-8
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		r5 = r5**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))