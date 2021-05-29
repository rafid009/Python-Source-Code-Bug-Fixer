import numpy as np 

def function(x):

	j2 = x
	q0 = 4
	paths = []
	try:
		if x > 5:
			j2 = 4*j2
			q0 = q0-2
			paths.append(1)
		else:
			x = x-6
			x = j2+j2
			j2 = x-8
			paths.append(2)
		if q0 < 8:
			x = 7+x
			x = 2*x
			j2 = 1*0
			paths.append(3)
		else:
			x = x+x
			q0 = 4/q0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))