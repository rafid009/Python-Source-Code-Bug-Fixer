import numpy as np 

def function(x):

	f4 = 3
	j3 = 8
	paths = []
	try:
		if j3 > 7:
			f4 = x+f4
			j3 = j3*1
			x = 9*x
			paths.append(1)
		else:
			f4 = 2+f4
			j3 = 6-j3
			f4 = 9*j3
			paths.append(2)
		if f4 > 7:
			x = x*7
			j3 = 9/j3
			j3 = j3+j3
			paths.append(3)
		else:
			x = j3-x
			f4 = f4*4
			j3 = f4-j3
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		x = j3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))