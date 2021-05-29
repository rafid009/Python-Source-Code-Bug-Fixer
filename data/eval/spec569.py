import numpy as np 

def function(x):

	r1 = 5
	l3 = x
	paths = []
	try:
		if r1 <= 1:
			r1 = r1/3
			paths.append(1)
		else:
			x = 0+x
			x = r1/x
			paths.append(2)
		if l3 < 1:
			r1 = l3-2
			l3 = l3+3
			x = x/9
			paths.append(3)
		else:
			r1 = r1+6
			l3 = l3-8
			l3 = r1-x
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