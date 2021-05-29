import numpy as np 

def function(x):

	f9 = x
	j3 = 2
	paths = []
	try:
		if f9 >= 7:
			j3 = 3+j3
			x = 4+x
			paths.append(1)
		else:
			f9 = 9*f9
			x = x*j3
			paths.append(2)
		if f9 <= 8:
			j3 = j3*1
			f9 = 1/x
			x = 4+x
			paths.append(3)
		else:
			j3 = j3/6
			f9 = 7+f9
			j3 = 3-j3
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