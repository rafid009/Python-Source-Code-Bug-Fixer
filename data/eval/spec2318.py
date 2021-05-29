import numpy as np 

def function(x):

	t2 = 5
	j3 = x
	x = x
	paths = []
	try:
		if t2 < 3:
			t2 = 1-0
			j3 = j3-j3
			x = x+x
			paths.append(1)
		else:
			j3 = j3*7
			j3 = j3-j3
			paths.append(2)
		if x < 9:
			j3 = j3-2
			t2 = 4*4
			paths.append(3)
		else:
			j3 = 8/x
			x = j3*t2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))