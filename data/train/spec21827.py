import numpy as np 

def function(x):

	f9 = x
	j3 = 6
	paths = []
	try:
		if f9 <= 0:
			j3 = 4*j3
			j3 = 3-j3
			paths.append(1)
		else:
			x = 9*2
			x = x-4
			paths.append(2)
		if j3 < 6:
			x = x+2
			j3 = x/x
			j3 = j3+j3
			paths.append(3)
		else:
			f9 = f9*x
			x = f9-x
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		x = f9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))