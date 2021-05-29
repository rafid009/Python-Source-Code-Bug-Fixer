import numpy as np 

def function(x):

	r1 = 1
	j5 = 1
	paths = []
	try:
		if r1 < 2:
			r1 = 4-r1
			r1 = j5/8
			paths.append(1)
		else:
			x = 5/x
			r1 = x*x
			x = x+4
			paths.append(2)
		if x > 0:
			r1 = r1-j5
			j5 = j5-8
			x = 7+x
			paths.append(3)
		else:
			j5 = 8*j5
			r1 = 1/2
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