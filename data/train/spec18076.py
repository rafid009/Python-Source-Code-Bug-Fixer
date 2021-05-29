import numpy as np 

def function(x):

	p1 = x
	r7 = x
	paths = []
	try:
		if r7 < 7:
			x = x+p1
			r7 = r7*9
			x = 5*x
			paths.append(1)
		else:
			x = 6/x
			r7 = p1-1
			p1 = 7*7
			paths.append(2)
		if r7 >= 2:
			r7 = 6*5
			x = 5+x
			paths.append(3)
		else:
			x = 3-8
			r7 = r7-6
			p1 = p1+r7
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		r7 = r7**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))