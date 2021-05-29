import numpy as np 

def function(x):

	v5 = x
	j2 = 4
	paths = []
	try:
		if x < 5:
			v5 = 3-2
			x = x/2
			paths.append(1)
		else:
			j2 = 4/x
			x = 2*x
			v5 = 1*5
			paths.append(2)
		if v5 > 1:
			j2 = 4-j2
			x = x+6
			j2 = j2+v5
			paths.append(3)
		else:
			v5 = v5-j2
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