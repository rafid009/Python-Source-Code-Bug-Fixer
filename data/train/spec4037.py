import numpy as np 

def function(x):

	j3 = 0
	t0 = 4
	paths = []
	try:
		if x <= 1:
			x = 5*x
			x = 0+3
			j3 = t0-j3
			paths.append(1)
		else:
			x = j3-x
			paths.append(2)
		if x <= 4:
			j3 = 8*j3
			x = x*8
			t0 = 9/x
			paths.append(3)
		else:
			x = 8-x
			x = x-1
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		j3 = t0**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))