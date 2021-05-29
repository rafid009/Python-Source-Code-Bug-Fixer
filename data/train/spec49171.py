import numpy as np 

def function(x):

	r8 = x
	j2 = x
	paths = []
	try:
		if x > 4:
			r8 = r8-6
			paths.append(1)
		else:
			x = x*r8
			x = x*9
			j2 = j2-4
			paths.append(2)
		if j2 >= 0:
			r8 = r8/4
			paths.append(3)
		else:
			j2 = 9*r8
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))