import numpy as np 

def function(x):

	j5 = x
	r1 = x
	paths = []
	try:
		if x >= 4:
			r1 = 0/r1
			j5 = r1+j5
			paths.append(1)
		else:
			x = 4-x
			j5 = j5+0
			x = j5/4
			paths.append(2)
		if r1 < 7:
			x = 8+r1
			r1 = r1-2
			paths.append(3)
		else:
			r1 = x+x
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		x = r1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))