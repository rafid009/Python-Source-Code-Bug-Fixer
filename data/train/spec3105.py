import numpy as np 

def function(x):

	j9 = x
	r1 = x
	x = 4
	paths = []
	try:
		if x <= 3:
			x = x*5
			j9 = 7*j9
			paths.append(1)
		else:
			r1 = 1/r1
			paths.append(2)
		if j9 < 9:
			j9 = 7*2
			j9 = 0/j9
			paths.append(3)
		else:
			r1 = r1-5
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		j9 = r1**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))