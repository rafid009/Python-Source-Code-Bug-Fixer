import numpy as np 

def function(x):

	r1 = x
	j2 = 8
	x = x
	paths = []
	try:
		if x < 9:
			r1 = x*3
			x = 5+x
			paths.append(1)
		else:
			x = r1-2
			r1 = 6+r1
			r1 = r1+5
			paths.append(2)
		if j2 >= 5:
			x = 4/x
			x = x+5
			paths.append(3)
		else:
			x = 8+x
			j2 = 8+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))