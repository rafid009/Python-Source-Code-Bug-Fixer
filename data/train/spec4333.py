import numpy as np 

def function(x):

	r0 = x
	j2 = x
	x = x
	paths = []
	try:
		if x >= 7:
			x = x+0
			j2 = x-8
			paths.append(1)
		else:
			j2 = 1+r0
			paths.append(2)
		if x < 9:
			j2 = j2-j2
			j2 = j2*r0
			paths.append(3)
		else:
			x = 2+x
			x = x*5
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