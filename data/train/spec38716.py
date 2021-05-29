import numpy as np 

def function(x):

	r4 = 6
	j3 = 6
	paths = []
	try:
		if x < 5:
			x = 2*r4
			r4 = r4*r4
			r4 = 7-r4
			paths.append(1)
		else:
			r4 = r4/6
			paths.append(2)
		if j3 < 9:
			x = r4/7
			j3 = j3+x
			j3 = j3/2
			paths.append(3)
		else:
			x = 8-0
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		j3 = r4**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))