import numpy as np 

def function(x):

	r1 = x
	i7 = 4
	paths = []
	try:
		if x <= 4:
			r1 = 9/8
			paths.append(1)
		else:
			r1 = 1+r1
			paths.append(2)
		if r1 < 6:
			r1 = 3-r1
			i7 = i7+1
			paths.append(3)
		else:
			i7 = 6-2
			x = x*9
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