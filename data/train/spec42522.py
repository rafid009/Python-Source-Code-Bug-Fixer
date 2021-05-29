import numpy as np 

def function(x):

	d7 = x
	j2 = 2
	paths = []
	try:
		if j2 >= 1:
			x = d7+1
			j2 = j2*j2
			j2 = j2*7
			paths.append(1)
		else:
			j2 = j2+8
			j2 = j2-0
			paths.append(2)
		if d7 < 0:
			j2 = j2*j2
			j2 = x/j2
			x = j2*x
			paths.append(3)
		else:
			j2 = j2*4
			x = x*x
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		d7 = d7**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))