import numpy as np 

def function(x):

	j6 = 5
	r7 = 8
	paths = []
	try:
		if x <= 1:
			x = x+j6
			r7 = r7+x
			r7 = 5/7
			paths.append(1)
		else:
			r7 = r7/2
			r7 = 7+6
			paths.append(2)
		if x < 1:
			r7 = x*r7
			x = x*7
			paths.append(3)
		else:
			j6 = j6/j6
			j6 = j6*j6
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		j6 = r7**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))