import numpy as np 

def function(x):

	j6 = x
	r9 = 7
	paths = []
	try:
		if j6 <= 4:
			j6 = 4*x
			paths.append(1)
		else:
			x = 9-x
			x = r9-3
			paths.append(2)
		if x > 0:
			j6 = 4+r9
			paths.append(3)
		else:
			x = 5*r9
			r9 = 3-r9
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		j6 = r9**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))