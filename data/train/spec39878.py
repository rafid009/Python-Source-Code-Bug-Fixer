import numpy as np 

def function(x):

	r0 = x
	j0 = x
	paths = []
	try:
		if x < 8:
			j0 = j0*6
			x = x/r0
			r0 = r0/6
			paths.append(1)
		else:
			r0 = 3*2
			j0 = 8+j0
			x = x+x
			paths.append(2)
		if x > 7:
			j0 = x*1
			x = 6/x
			paths.append(3)
		else:
			j0 = j0-8
			x = x*x
			j0 = 2+j0
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		j0 = r0**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))